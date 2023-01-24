import unittest
from selenium import webdriver
import time
from test_baidu.baidu_page1 import BaiduPage
from selenium.webdriver import Remote, DesiredCapabilities
# from HTMLTestRunner_cn import HTMLTestRunner


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Remote(desired_capabilities=DesiredCapabilities.FIREFOX.copy())
        cls.driver.maximize_window()

    def test_search_key_case1(self):
        """ 测试标题一致 """
        dr = BaiduPage(self.driver)
        dr.open(BaiduPage.url)
        dr.input = 'selenium'
        dr.button.click()
        time.sleep(2)
        a = dr.button.is_displayed()
        self.assertTrue(a, '可见')  # add assertion here

    def test_search_key_case2(self):
        """ 测试标题不一致报错 """
        dr = BaiduPage(self.driver)
        dr.open(BaiduPage.url)
        dr.input = 'pageobject'
        dr.button.click()
        time.sleep(2)
        self.assertEqual(self.driver.title, 'selenium' + '_百度搜索', '标题一致')  # add assertion here

    def test_search_key_case3(self):
        """ 大小写不一致报错 """
        dr = BaiduPage(self.driver)
        dr.open(BaiduPage.url)
        dr.input = 'python'
        dr.button.click()
        time.sleep(2)

        self.assertEqual(self.driver.title, 'Python' + '_百度搜索', '大小写不一致会报错')  # add assertion here

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()




if __name__ == '__main__':
    test_dir = './'
    suit = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    runner = unittest.TextTestRunner()
    """now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
    address = './' + now_time + 'result.html'
    with open(address, 'wb') as fp:
        runner = HTMLTestRunner(stream=address,
                                title='测试百度搜索',
                                description='Windows11,Chrome环境'
                                )"""
    runner.run(suit)

    # unittest.main(verbosity=2)
