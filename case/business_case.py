# -*- coding: utf-8 -*-
# @Time : 2020/12/30 9:55
# @Author : 唐涛
# @Email : 2410725336@qq.com
# @File : business_case.py
# @Project : crm2
from case.base_case import BaseCase
import unittest

from model.browser import chrome
from page.Business_page import BusinessPage
from page.login_page import LoginPage


class test_business(unittest.TestCase):
    def setUp(self) -> None:
        '''前置条件'''
        self.driver = chrome()
        lp = LoginPage(self.driver)
        lp.login('xiaotang', '123456')

    def test_1(self):
        BusinessPage(self.driver).business('98765445')
        a=BusinessPage(self.driver).successfully()
        self.assertIn('删除成功',a)

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()




