# -- coding: utf-8 --
import unittest
import time
from XTestRunner import HTMLTestRunner

test_dir = "C:/Users/52801/PycharmProjects/pythonProject/test_baidu/test_baidu_homepage"
suits = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == "__main__":
    now_time = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())
    address = "C:/Users/52801/PycharmProjects/pythonProject/test_baidu/test_baidu_homepage/" + now_time + "result.html"
    with open(address, "wb") as fp:
        runner = HTMLTestRunner(stream=fp,
                                title='百度首页',
                                description='Windows10,Chrome环境'
                                )
        runner.run(suits)




