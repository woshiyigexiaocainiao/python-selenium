# -- coding: utf-8 --
from poium import Page, Element


class BaiduPage(Page):
    url = 'https://www.baidu.com'
    input = Element(id_="kw", timeout=1, index=0, describe="搜索输入框")
    button = Element(id_="su", timeout=1, index=0, describe="搜索按钮")
    result = Element(partial_link_text="详解 - 百度文库", describe="搜索结果")


































