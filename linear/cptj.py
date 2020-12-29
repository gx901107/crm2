# -*- coding: utf-8 -*-
# @Time : 2020/12/28 22:19
# @Author : 唐涛
# @Email : 2410725336@qq.com
# @File : cptj.py
# @Project : crm2
from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from page.login_page import LoginPage
class MyTest_a(unittest.TestCase):

    '''测试a'''
    def test_sjtj(self):
        self.driver=webdriver.Chrome()
        LoginPage(self.driver).login('xiaotang','123456')
        sleep(3)
        self.driver.find_element_by_link_text('产品').click()
        sleep(1)
        self.driver.find_element_by_css_selector('body > div.container > div.row > div:nth-child(2) > div.pull-right > a').click()
        sleep(1)
        self.driver.find_element_by_css_selector('#name').send_keys('5873')
        sleep(1)
        self.driver.find_element_by_css_selector('#development_time').send_keys('2020-12-16')
        sleep(1)
        self.driver.find_element_by_css_selector('#development_team').send_keys('22')
        sleep(1)
        self.driver.find_element_by_css_selector('#suggested_price').send_keys('22')
        sleep(1)
        self.driver.find_element_by_css_selector('#cost_price').send_keys('22')
        sleep(1)
        self.driver.find_element_by_css_selector('#form1 > table > tfoot > tr > td > input:nth-child(1)').click()
        sleep(5)
if __name__ == '__main__':
    unittest.main()

