# -- coding: utf-8 --
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import unittest
import os
"""from dataclasses import dataclass


@dataclass
class A:
    x: int
    y: int

    def add(self):
        return self.x + self.y


a = A(2, 3)

print(a.add())"""


"""class Classname:
    @staticmethod
    def fun():
        print('静态方法')

    @classmethod
    def a(cls):
        print('类方法')

    # 普通方法
    def b(self):
        print('普通方法')


Classname.fun()
Classname.a()
C = Classname()
C.fun()
C.a()
C.b()"""


"""class Complex:
    r: int
    i: int

    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def add(self):
        return self.r + self.i


x = Complex(2, 3)
print(x.add())
print(x.r)
"""


"""driver = webdriver.Chrome()
driver.get('http://jqueryui.com/resources/demos/draggable/scroll.html')
onePosition = driver.find_element(By.ID, "draggable")
twoPosition = driver.find_element(By.ID, "draggable2")
sanPosition = driver.find_element(By.ID, "draggable3")
action_chains = ActionChains(driver)
action_chains.drag_and_drop(onePosition, twoPosition).perform()
for i in range(5):
    action_chains.drag_and_drop_by_offset(sanPosition, 10, 10).perform()
    time.sleep(2)
driver.close()"""

# 键盘操作和判断元素是否存在
"""driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')

driver.find_element(By.ID, 'kw').send_keys(Keys.F5)
time.sleep(2)
driver.find_element(By.ID, 'kw').send_keys(Keys.F5)
driver.find_element(By.ID, 'kw').send_keys('selenium')
time.sleep(2)
driver.find_element(By.ID, 'kw').send_keys(Keys.CONTROL, 'a')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#kw').send_keys(Keys.CONTROL, 'x')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#kw').send_keys(Keys.CONTROL, 'v')
try:
    ele = driver.find_element(By.ID, 'su1')
    if ele.is_displayed():
        ele.click()
except NoSuchElementException:
    print('没有找到点击按钮')

else:
    print('找到了点击按钮')

time.sleep(5)

driver.quit()"""


# 结束Windows窗口浏览器进程


"""class TestDemo(unittest.TestCase):
    def test_killWindowsProcess(self):
        chrome_driver = webdriver.Chrome()

        return_code = os.system("taskkill /f /t /im chrome.exe")
        if return_code == 0:
            print("chrome进程结束成功")


if __name__ == "__main__":
    unittest.main()"""


# input 上传文件
"""class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_uploadFile(self):
        self.driver.get("http://sahitest.com/demo/php/fileUpload.htm")
        upload = self.driver.find_element(By.ID, 'file')
        upload.send_keys('D:\\wx\\english.txt')  # send_keys
        time.sleep(3)
        print(upload.get_attribute('value'))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()"""

# 操作富文本框
"""driver = webdriver.Chrome()
driver.get('https://github.com/fex-team/ueditor')
time.sleep(10)
driver.switch_to.frame('repo-content-turbo-frame')  # 注意，这种editor一定有frame，一定要切frame

body_string = "Hello world again again!\
Hello world again again!\
Hello world again again!\
Hello world again again!"

driver.find_element(By.TAG_NAME, 'body').send_keys(body_string)  # 直接往frame里的body里填内容
print(driver.find_element(By.TAG_NAME, 'body').text)
driver.quit()"""


# 使用Chrome浏览器自动将文件下载到指定路径
"""class TestDemo(unittest.TestCase):
    def setUp(self):
        chromeOptions = webdriver.ChromeOptions()
        prefs = {'download.default_directory': 'C:\\Users\\52801\\Downloads'}
        chromeOptions.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome()

    def test_downloadFileByChrome(self):
        url = 'https://pypi.org/project/selenium/#files'
        self.driver.get(url)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "selenium-4.7.2.tar.gz").click()
        time.sleep(50)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()"""



driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element(By.ID, "kw").send_keys("软达启航")
driver.find_element(By.ID, "su").click()
time.sleep(3)
assert "软达启航" in driver.page_source, "页面源码中不存在该关键字"
driver.close()






