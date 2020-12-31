# -*- coding: utf-8 -*-
# @Time : 2020/12/30 11:35
# @Author : 唐涛
# @Email : 2410725336@qq.com
# @File : business1_case.py
# @Project : crm2
import unittest

from model.browser import chrome
from page.Business1_page import Business1Page
from page.login_page import LoginPage
class test_business1(unittest.TestCase):
    def setUp(self) -> None:
        '''前置条件'''
        self.driver = chrome()
        lp = LoginPage(self.driver)
        lp.login('xiaotang', '123456')

    def test_2(self):
        Business1Page(self.driver).business1()

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()