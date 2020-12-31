# -*- coding: utf-8 -*-
# @Time : 2020/12/30 11:45
# @Author : 唐涛
# @Email : 2410725336@qq.com
# @File : product_case.py
# @Project : crm2
import unittest
from model.browser import chrome
from page.login_page import LoginPage
from page.product_page import ProductPage
class test_product(unittest.TestCase):
    def setUp(self) -> None:
        '''前置条件'''
        self.driver = chrome()
        lp = LoginPage(self.driver)
        lp.login('xiaotang', '123456')

    def test_3(self):
        ProductPage(self.driver).product('234576543')

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()