# -*- coding: utf-8 -*-
# @Time : 2020/12/12 17:11
# @Author : fcj11
# @Email : yangfit@126.com
# @File : home_page.py
# @Project : crm自动化测试
from selenium.webdriver.common.by import By
from page.base_page import BasePage



class HomePage(BasePage):
    _url = BasePage._url + '/crm/index.php?m=leads'

    clue_locator = (By.LINK_TEXT, '线索')  #定位线索
    client_locator = (By.CSS_SELECTOR,'body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul:nth-child(1) > li:nth-child(2) > a')  #定位客户
    opportunity_locator = (By.CSS_SELECTOR, 'body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul:nth-child(1) > li:nth-child(3) > a')  #定位商机


    def click_clue(self):  #点击线索
        self.find_element(self.clue_locator).click()
    def click_client(self):  #点击客户
        self.find_element(self.client_locator).click()
    def click_opportunity(self):  #点击商机
        self.find_element(self.opportunity_locator).click()



