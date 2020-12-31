# -*- coding: utf-8 -*-
# @Time : 2020/12/12 18:46
# @Author : fcj11
# @Email : yangfit@126.com
# @File : base_page.py
# @Project : crm自动化测试
from selenium.webdriver.remote.webelement import WebElement


class BasePage():
    """页面类的基类"""
    _url = 'http://192.168.1.213'  # 基类url的服务器地址

    def __init__(self, driver, url=None):
        self.driver = driver
        if not url:
            url = self._url
        self.url = url

    def find_element(self, locator, element=None):  # 封装find_element
        # return self.driver.find_element(*locator)
        if element and isinstance(element, WebElement):
            return element.find_element(*locator)
        return self.driver.find_element(*locator)

    def find_elements(self, locator, element=None):  # 封装find_elements
        if element and isinstance(element, WebElement):
            return element.find_elements(*locator)
        return self.driver.find_elements(*locator)

    def switch_to(self):
        self.driver.switch_to.alert.accept()
    def switch_dissmiss(self):
        self.driver.switch_to.alert.dismiss()
    def switchparent_frame(self):
        self.driver.switch_to.parent_frame()
    def switch_frame(self,frame):
        self.driver.switch_to.frame(frame)

