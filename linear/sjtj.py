# -*- coding: utf-8 -*-
# @Time : 2020/12/28 21:56
# @Author : 唐涛
# @Email : 2410725336@qq.com
# @File : sjtj.py
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
        #点击商机
        self.driver.find_element_by_link_text('商机').click()
        #点击统计
        self.driver.find_element_by_css_selector('body > div.container > div.page-header > ul > li:nth-child(2) > a').click()
        sleep(3)
        locator=self.driver.find_element_by_css_selector('#department')   #定位到选择部门下拉菜单
        select=Select(locator)
        select.select_by_index(1)    #为选择部门赋值
        sleep(3)
        locator=self.driver.find_element_by_css_selector('#role')   #定位到选择员工下拉菜单
        select=Select(locator)
        select.select_by_index(1)    #为选择员工赋值
        sleep(3)
        self.driver.find_element_by_css_selector('#start_time').send_keys('2020-12-01')
        sleep(3)
        self.driver.find_element_by_css_selector('#end_time').send_keys('2020-12-03')
        sleep(1)
        self.driver.find_element_by_css_selector('#searchForm > ul > li:nth-child(4) > button').click()#搜索
        sleep(2)
        self.driver.find_element_by_link_text('选择统计内容').click()
        sleep(1)
        self.driver.find_element_by_css_selector('#show_report').click()
        sleep(1)
        self.driver.find_element_by_css_selector('#show_status').click()
        sleep(1)
        self.driver.find_element_by_css_selector('#show_money').click()
        sleep(1)
        self.driver.find_element_by_css_selector('#show_source').click()
        sleep(1)
        self.driver.find_element_by_css_selector('#show_day').click()
        sleep(1)
        self.driver.find_element_by_css_selector('#show_week').click()
        sleep(1)
        self.driver.find_element_by_css_selector('#show_month').click()
        sleep(1)
if __name__ == '__main__':
    unittest.main()


