# -*- coding: utf-8 -*-
# @Time : 2020/12/29 22:44
# @Author : 唐涛
# @Email : 2410725336@qq.com
# @File : product1_page.py
# @Project : crm2
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from page.base_page import BasePage
class Product1Page(BasePage):
    '''产品搜索页面'''
    product_locator = (By.LINK_TEXT,'产品') # 产品
    any_field_locator=(By.CSS_SELECTOR,'#field')#任意字段
    include_locator=(By.CSS_SELECTOR,'#condition')#包含
    search_box_locator=(By.CSS_SELECTOR,'#search')#搜素框
    search_locator=(By.CSS_SELECTOR,'#dosearch')#搜索

    def click_product(self):#产品
        self.find_element(self.product_locator).click()
    def click_any_field(self):#任意字段
        select = Select(self.find_element(self.any_field_locator))
        select.select_by_index(1)
    def click_include(self):#包含
        select = Select(self.find_element(self.include_locator))
        select.select_by_index(1)
    def input_search_box(self):#搜索框
        self.find_element(self.search_box_locator).send_keys('宇宙')
    def click_search(self):#搜索
        self.find_element(self.search_locator).click()

