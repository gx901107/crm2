# -*- coding: utf-8 -*-
# @Time : 2020/12/29 22:18
# @Author : 唐涛
# @Email : 2410725336@qq.com
# @File : product_page.py
# @Project : crm2
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
from page.base_page import BasePage
class ProductPage(BasePage):
    '''产品添加页面类'''
    product_locator=(By.LINK_TEXT,'产品')#产品
    add_product_locator=(By.CSS_SELECTOR,'body > div.container > div.row > div:nth-child(2) > div.pull-right > a')#添加产品
    product_name_locator=(By.CSS_SELECTOR,'#name')#产品名称
    development_time_locator=(By.CSS_SELECTOR,'#development_time')#研发时间
    development_team_locator=(By.CSS_SELECTOR,'#development_team')#开发团队
    retail_price_locator=(By.CSS_SELECTOR,'#suggested_price')#建议售价
    cost_price_locator=(By.CSS_SELECTOR,'#cost_price')#成本价
    save_locator=(By.CSS_SELECTOR,'#form1 > table > tfoot > tr > td > input:nth-child(1)')#保存
    table_locator = (By.CSS_SELECTOR, '#form1 > table')  # 表格
    tr_locator=(By.TAG_NAME,'tr')#tr标签
    td_locator=(By.TAG_NAME,'td')#td标签
    a_locator=(By.TAG_NAME,'a')#a标签
    affirm_locator = (By.CSS_SELECTOR,'body > div.container > div.alert.alert-success')  # 断言

    def click_product(self):#产品
        self.find_element(self.product_locator).click()
    def click_add_product(self):#添加产品
        self.find_element(self.add_product_locator).click()
    def input_product_name(self,number):#产品名称
        self.find_element(self.product_name_locator).send_keys(number)
    def input_development_time(self):#研发时间
        self.find_element(self.development_time_locator).send_keys('2020-12-16')
    def input_development_team(self):#开发团队
        self.find_element(self.development_team_locator).send_keys('22')
    def input_retail_price(self):#建议售价
        self.find_element(self.retail_price_locator).send_keys('22')
    def input_cost_price(self):#成本价
        self.find_element(self.cost_price_locator).send_keys('22')
    def click_save(self):#保存
        self.find_element(self.save_locator).click()

    def assertions_search(self, clientname1):
        element = self.find_element(self.table_locator)
        tr_list = self.find_elements(self.tr_locator, element)[2:]
        for tr in tr_list:
            td_list = self.find_elements(self.td_locator, tr)
            if td_list[1].text == clientname1:
                return td_list[1].text
    def affirm(self):
        return self.find_element(self.affirm_locator).text

    def product(self,number):
        self.click_product()#产品
        sleep(2)
        self.click_add_product()#添加产品
        sleep(2)
        self.input_product_name(number)#产品名称
        sleep(2)
        self.input_development_time()#研发时间
        sleep(2)
        self.input_development_team()#开发团队
        sleep(2)
        self.input_retail_price()#建议售价
        sleep(2)
        self.input_cost_price()#成本价
        sleep(2)
        self.click_save()#保存
        sleep(2)














