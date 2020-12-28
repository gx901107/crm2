# -*- coding: utf-8 -*-
# @Time : 2020/12/12 19:46
# @Author : fcj11
# @Email : yangfit@126.com
# @File : base_case.py
# @Project : crm自动化测试
import unittest
from model.browser import chrome
from page.login_page import LoginPage

class BaseCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = chrome()
        lp = LoginPage(self.driver)
        lp.login('xiaoyang','123456')


    def tearDown(self) -> None:
        self.driver.quit()