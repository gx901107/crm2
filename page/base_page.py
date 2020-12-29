# -*- coding: utf-8 -*-
# @Time : 2020/12/12 18:46
# @Author : fcj11
# @Email : yangfit@126.com
# @File : base_page.py
# @Project : crm自动化测试
class BasePage():
    """页面类的基类"""
    _url = 'http://192.168.1.213'  # 基类url的服务器地址

    def __init__(self, driver, url=None):
        self.driver = driver
        if not url:
            url = self._url
        self.url = url

    def find_element(self,locator):
        return self.driver.find_element(*locator)