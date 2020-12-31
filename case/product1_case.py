# -*- coding: utf-8 -*-
# @Time : 2020/12/30 11:54
# @Author : 唐涛
# @Email : 2410725336@qq.com
# @File : product1_case.py
# @Project : crm2
import unittest
from model.browser import chrome
from page.login_page import LoginPage
from page.product1_page import Product1Page

class test_product1(unittest.TestCase):
    def setUp(self) -> None:
        '''前置条件'''
        self.driver = chrome()
        lp = LoginPage(self.driver)
        lp.login('xiaotang', '123456')
    def test_4(self):

        a=Product1Page(self.driver)
        a.product1()
        b=a.assertions_search('234576543')
        print(b)

        # self.assertEqual(self)
    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()