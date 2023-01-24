# -- coding: utf-8 --
from base import BasePage


class BaiduPage(BasePage):
    url = 'https://www.baidu.com'

    # 百度page层，百度页面封装操作到的元素。。。
    def search_input(self, search_keys):
        self.by_id("kw").send_keys(search_keys)     # 百度输入框定位

    def search_button(self):
        self.by_id('su').click()




















