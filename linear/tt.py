# -*- coding: utf-8 -*-
# @Time : 2020/12/28 15:51
# @Author : 唐涛
# @Email : 2410725336@qq.com
# @File : tt.py
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
        # driver.get('http://192.168.1.213/crm/index.php?m=user&a=login')
        # sleep(3)
        LoginPage(self.driver).login('xiaotang','123456')
        sleep(3)
        self.driver.find_element_by_link_text('商机').click()
        sleep(3)
        self.driver.find_element_by_class_name('btn-primary').click()
        sleep(3)
        self.driver.find_element_by_id('owner_name').click()
        sleep(3)
        self.driver.find_element_by_css_selector('#d_content > tr:nth-child(1) > td:nth-child(1) > input[type=radio]').click()
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[12]/div[3]/div/button[1]/span').click()
        sleep(3)
        self.driver.find_element_by_name('customer_name').click()
        sleep(3)
        self.driver.find_element_by_name('customer').click()
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[10]/div[3]/div/button[1]/span').click()
        sleep(3)
        self.driver.find_element_by_name('total_price').send_keys("1234")
        sleep(3)
        self.driver.find_element_by_css_selector('#name').send_keys('5987634')
        sleep(3)
        self.driver.find_element_by_name('contacts_name').click()
        sleep(3)
        self.driver.find_element_by_name('contacts').click()
        sleep(3)
        self.driver.find_element_by_css_selector('body > div:nth-child(18) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(1)').click()
        sleep(3)
        locator=self.driver.find_element_by_css_selector('#type') #定位到商机类型下拉框菜单
        select=Select(locator)
        select.select_by_index(1)    #为商机类型赋值第一个
        self.driver.find_element_by_css_selector('#form1 > table > tbody > tr:nth-child(5) > td:nth-child(2) > input').send_keys('和平街')
        sleep(3)
        locator=self.driver.find_element_by_css_selector('#origin')#定位到商机来源下拉框
        select=Select(locator)
        select.select_by_index(1)    #为商机来源赋值第一个
        sleep(3)
        locator=self.driver.find_element_by_css_selector('#status_id')#定位到状态下拉框
        select=Select(locator)
        select.select_by_index(1)   #为状态赋值第一个
        sleep(3)
        self.driver.find_element_by_id('gain_rate').send_keys('20')
        sleep(1)
        self.driver.find_element_by_id('estimate_price').send_keys('100')
        sleep(1)
        self.driver.find_element_by_id('nextstep_time').send_keys('2020-12-01 16:28')
        sleep(1)
        self.driver.find_element_by_id('nextstep').send_keys('不知道')
        sleep(1)
        self.driver.find_element_by_id('description').send_keys('不知道哦')
        self.driver.find_element_by_css_selector('#form1 > table > tbody > tr:nth-child(12) > th > input').click()
        sleep(1)
        self.driver.find_element_by_css_selector('#data > tr > td:nth-child(1) > input.product_id').click()
        sleep(3)
        self.driver.find_element_by_css_selector('body > div:nth-child(22) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(1) > span').click()
        sleep(3)
        self.driver.find_element_by_css_selector('#form1 > table > tfoot > tr > td > input:nth-child(1)').click()
        sleep(1)
        locator = self.driver.find_element_by_css_selector('#field')   #定位到请选择筛选条件
        select = Select(locator)
        select.select_by_index(1)    #为请选择筛选条件赋值
        sleep(3)
        # locator=self.driver.find_element_by_css_selector('#search')   #定位到包含
        # select = Select(locator)
        # select.select_by_index(1)      #为定位赋值
        # sleep(3)
        self.driver.find_element_by_css_selector('#dosearch').click()
        sleep(3)
        locator = self.driver.find_element_by_css_selector('#field')  # 定位到请选择筛选条件
        select = Select(locator)
        select.select_by_index(0)  # 为请选择筛选条件赋值
        sleep(3)
        self.driver.find_element_by_css_selector('#dosearch').click()
        sleep(3)
        self.driver.switch_to.alert.accept()#确定警告框
        sleep(1)
        self.driver.find_element_by_css_selector('#form1 > table > tbody > tr > td:nth-child(12) > a:nth-child(1)').click()
        sleep(2)
        self.driver.find_element_by_css_selector('#tab1 > div.container2.top-pad > div > a:nth-child(3)').click()
        sleep(1)
        self.driver.find_element_by_css_selector('#form1 > table > tbody > tr > td:nth-child(12) > a:nth-child(3)').click()
        sleep(1)
        self.driver.find_element_by_css_selector('#total_price').send_keys('200')
        sleep(1)
        self.driver.find_element_by_css_selector('body > div.container > div.row > div > form > table > tfoot > tr > td > input.btn.btn-primary').click()
        sleep(1)
        self.driver.find_element_by_css_selector('#form1 > table > tbody > tr > td:nth-child(1) > input').click()
        sleep(1)
        self.driver.find_element_by_css_selector('#delete').click()
        sleep(3)
        # self.driver.find_element_by_id('confirm').click()      #点击出现一个警告框
        # self.driver.switch_to.confirm.text     #或许alert上的文本
        self.driver.switch_to.alert.accept()    #确定警告框
        sleep(3)

if __name__ == '__main__':
    unittest.main()

