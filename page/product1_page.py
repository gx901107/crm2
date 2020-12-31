# -*- coding: utf-8 -*-
# @Time : 2020/12/29 22:44
# @Author : 唐涛
# @Email : 2410725336@qq.com
# @File : product1_page.py
# @Project : crm2
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
from page.base_page import BasePage
class Product1Page(BasePage):
    '''产品搜索页面'''
    product_locator = (By.LINK_TEXT,'产品') # 产品
    any_field_locator=(By.CSS_SELECTOR,'#field')#任意字段
    include_locator=(By.CSS_SELECTOR,'#condition')#包含
    search_box_locator=(By.CSS_SELECTOR,'#search')#搜素框
    search_locator=(By.CSS_SELECTOR,'#dosearch')#搜索
    examine_locator=(By.CSS_SELECTOR,'#form1 > table > tbody > tr:nth-child(1) > td:nth-child(6) > a:nth-child(1)')#查看
    return_locator=(By.CSS_SELECTOR,'#tab1 > div.container2.top-pad > div > a:nth-child(3)')#返回
    compile_locator=(By.CSS_SELECTOR,'#form1 > table > tbody > tr:nth-child(1) > td:nth-child(6) > a:nth-child(2)')#编辑
    edit_content_locator=(By.CSS_SELECTOR,'#development_team')#编辑内容
    save_locator=(By.CSS_SELECTOR,'#form1 > table > tfoot > tr > td > input.btn.btn-primary')#保存
    product_tool_locator=(By.CSS_SELECTOR,'body > div.container > div.row > div:nth-child(2) > div.pull-right > div > button')#产品工具
    export_products_locator=(By.CSS_SELECTOR,'#excelExport')#导出产品
    table_locator=(By.CSS_SELECTOR,'#form1 > table')#表格
    tr_locator=(By.TAG_NAME,'tr')#tr标签
    td_locator=(By.TAG_NAME,'td')#td标签
    a_locator=(By.TAG_NAME,'a')#a标签
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
    def click_examine(self):#查看
        self.find_element(self.examine_locator).click()
    def click_return(self):#返回
        self.find_element(self.return_locator).click()
    def click_compile(self):#编辑
        self.find_element(self.compile_locator).click()
    def input_edit_content(self):#编辑内容
        self.find_element(self.edit_content_locator).send_keys('2')
    def click_save(self):#保存
        self.find_element(self.save_locator).click()
    def click_product_tool(self):#产品工具
        self.find_element(self.product_tool_locator).click()
    def click_export_products(self):#导出产品
        self.find_element(self.export_products_locator).click()
        self.driver.switch_to.alert.accept()
    def assertions_search(self,clientname1):
        element = self.find_element(self.table_locator)
        tr_list = self.find_elements(self.tr_locator, element)[2:]
        for tr in tr_list:
            td_list = self.find_elements(self.td_locator, tr)
            if td_list[1].text == clientname1:
                return td_list[1].text


    def product1(self):
        self.click_product()#产品
        sleep(2)
        self.click_any_field()#任意字段
        sleep(2)
        self.click_include()#包含
        sleep(2)
        self.input_search_box()#搜索框
        sleep(2)
        self.click_search()#搜索
        sleep(2)
        self.click_examine()#查看
        sleep(2)
        self.click_return()#返回
        sleep(2)
        self.click_compile()#编辑
        sleep(2)
        self.input_edit_content()#编辑内容
        sleep(2)
        self.click_save()#保存
        sleep(2)
        self.click_product_tool()#产品工具
        sleep(2)
        self.click_export_products()#导出产品
        sleep(2)




















