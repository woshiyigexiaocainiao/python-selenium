# -- coding: utf-8 --
from selenium import webdriver
import time
import unittest
import ddt
from HTMLTestRunner_cn import HTMLTestRunner
from selenium.webdriver.common.by import By


@ddt.ddt
class login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = "https://www.zonghenggongkao.cn/#/comlogin"
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def zongheng_login(self, username, password):
        self.driver.get(self.url)
        self.driver.find_element(By.CSS_SELECTOR, "#item1").clear()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#item1").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "#item").clear()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#item").send_keys(password)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#app > div > div.computer > div > div > div > div.contentLeft >\
         div.conRightR > ul > li:nth-child(5) > button").click()
        time.sleep(2)

    @ddt.file_data("ddt_data_file.json")
    def test_login_case1(self, username, password):
        print(username, ":", password)
        self.zongheng_login(username, password)
        self.assertIn("活动区", self.driver.page_source, "登录成功")

    @classmethod
    def teardownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)











