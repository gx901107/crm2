# -*- coding: utf-8 -*-
# @Time : 2020/12/28 22:38
# @Author : 唐涛
# @Email : 2410725336@qq.com
# @File : cpss.py
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
        locator=self.driver.find_element_by_css_selector('#field')#定位到任意字段
        select=Select(locator)
        select.select_by_index(1)#为任意字段赋值
        sleep(3)
        locator=self.driver.find_element_by_css_selector('#condition')#定位到包含
        select=Select(locator)
        select.select_by_index(1) #为包含赋值
        sleep(3)
        self.driver.find_element_by_css_selector('#search').send_keys('宇宙')
        sleep(2)
        self.driver.find_element_by_css_selector('#dosearch').click()
        sleep(2)
        self.driver.find_element_by_css_selector('#form1 > table > tbody > tr:nth-child(1) > td:nth-child(6) > a:nth-child(1)').click()
        sleep(2)
        self.driver.find_element_by_css_selector('#tab1 > div.container2.top-pad > div > a:nth-child(3)').click()
        sleep(2)
        self.driver.find_element_by_css_selector('#form1 > table > tbody > tr:nth-child(1) > td:nth-child(6) > a:nth-child(2)').click()
        sleep(2)
        self.driver.find_element_by_css_selector('#development_team').send_keys('2')
        sleep(2)
        self.driver.find_element_by_css_selector('#form1 > table > tfoot > tr > td > input.btn.btn-primary').click()
        sleep(2)
        self.driver.find_element_by_css_selector('body > div.container > div.row > div:nth-child(2) > div.pull-right > div > button').click()
        sleep(2)
        self.driver.find_element_by_css_selector('#excelExport').click()
        sleep(2)
        self.driver.switch_to.alert.accept()
        sleep(3)
if __name__ == '__main__':
    unittest.main()

