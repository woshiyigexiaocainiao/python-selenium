# -- coding: utf-8 --
from selenium.webdriver.common.by import By


class BasePage:  # 定义父类
    """封装一些常用方法"""

    def __init__(self, driver):
        self.driver = driver

    def open(self, url=None):
        if url is None:
            self.driver.get(self.url)
        else:
            self.driver.get(url)
    # id 定位

    def by_id(self, id_):
        return self.driver.find_element(By.ID, id_)

    # name定位
    def by_name(self, name):
        return self.driver.find_element(By.ID, name)

    # class定位
    def by_class(self, class_name):
        return self.driver.find_element(By.ID, class_name)

    # Xpath定位
    def by_Xpath(self, xpath):
        return self.driver.find_element(By.ID, xpath)

    # Css定位
    def by_Css(self, css):
        return self.driver.find_element(By.ID, css)

    # link_Text定位
    def by_link_text(self, link_text):
        return self.driver.find_element(By.LINK_TEXT, link_text)

    # partial_link_text定位
    def by_partial_link_text(self, partial_link_text):
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, partial_link_text)

    # tar_name定位
    def by_tar_name(self, tar_name):
        return self.driver.find_element(By.TAG_NAME, tar_name)

    # 获取title
    def get_title(self):
        return self.driver.title

    # 获取页面text，仅使用Css定位获取
    def get_text(self, css):
        return self.by_Css(css).text

    # 执行JavaScript脚本
    def js(self, script):
        self.driver.execute_script(script)







