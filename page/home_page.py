# -*- coding: utf-8 -*-
# @Time : 2020/12/12 17:11
# @Author : fcj11
# @Email : yangfit@126.com
# @File : home_page.py
# @Project : crm自动化测试
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.login_page import LoginPage


class HomePage(BasePage):
    _url = BasePage._url + '/crm/index.php?m=leads'

    clue_locator = (By.LINK_TEXT, '线索')  #定位线索
    client_locator = (By.CSS_SELECTOR,'body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul:nth-child(1) > li:nth-child(2) > a')  #定位客户
    opportunity_locator = (By.CSS_SELECTOR, 'body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul:nth-child(1) > li:nth-child(3) > a')  #定位商机

    searchform_locator=(By.CSS_SELECTOR,'#searchForm > div > ul.list0.pull-right > li:nth-child(2) > input') #输入查询用户名
    searchbtn_locator=(By.CSS_SELECTOR,'#searchBtn') #查询按钮
    all_locator =(By.CSS_SELECTOR,'body > div.container > div.row > div.span3.knowledgecate > div > div.dynamiccate > ul:nth-child(1) > li:nth-child(1) > a') #全部动态
    previous_page_locator =(By.CSS_SELECTOR,'body > div.container > div.row > div.span9 > div > div.pagination > div.span4 > div > ul > li:nth-child(4) > a') #上一页
    next_page_locator =(By.CSS_SELECTOR,'body > div.container > div.row > div.span9 > div > div.pagination > div.span4 > div > ul > li:nth-child(2) > a') #下一页
    last_page_locator =(By.CSS_SELECTOR,'body > div.container > div.row > div.span9 > div > div.pagination > div.span4 > div > ul > li:nth-child(5) > a') #末页
    home_page_locator =(By.CSS_SELECTOR,'body > div.container > div.row > div.span9 > div > div.pagination > div.span4 > div > ul > li:nth-child(1) > a') #首页
    my_task_locator =(By.CSS_SELECTOR,'body > div.container > div.row > div.span3.knowledgecate > div > div.personal-panel > div:nth-child(2) > p:nth-child(4) > a:nth-child(1)') #我的任务
    all_task_locator = (By.CSS_SELECTOR, '/html/body/div[5]/p/a[1]') #全部任务
    _locator = (By.CSS_SELECTOR, '')
    _locator = (By.CSS_SELECTOR, '')
    _locator = (By.CSS_SELECTOR, '')
    _locator = (By.CSS_SELECTOR, '')

    def click_clue(self):  #点击线索
        self.find_element(self.clue_locator).click()
    def click_client(self):  #点击客户
        self.find_element(self.client_locator).click()
    def click_opportunity(self):  #点击商机
        self.find_element(self.opportunity_locator).click()



