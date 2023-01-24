# -- coding: utf-8 --
"""import time

from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By


class TestUrl(unittest.TestCase):

    def setUp(self):
        self.driverOne = webdriver.Chrome()
        self.driverOne.maximize_window()

    def test_url(self):
        self.driverOne.get('https://www.zonghenggongkao.cn')
        """
"""assert '纵横公考' in self.driverOne.current_url, '获取的是标题，应获取地址'
        print(self.driverOne.current_url)"""
"""
        self.driverOne.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/div/ul/li[1]').click()
        time.sleep(3)

    def tearDown(self):
        self.driverOne.quit()


if __name__ == '__main__':
    unittest.main()"""


class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent')

    def bar(self, message):
        print("%s from Parent" % message)


class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
        super(FooChild, self).__init__()
        print('Child')

    def bar(self, message):
        super(FooChild, self).bar(message)
        print('Child bar fuction')
        print(self.parent)


if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')















