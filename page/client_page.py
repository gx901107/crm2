# -*- coding: utf-8 -*-
# @Time : 2020/12/12 22:08
# @Author : fcj11
# @Email : yangfit@126.com
# @File : client.py
# @Project : crm自动化测试
from time import sleep

from selenium.webdriver.common.by import By

from case.base_case import BaseCase
from page.base_page import BasePage
from page.home_page import HomePage

class NewClient(BasePage):
    """定位器"""
    """定位客户列表表格"""
    table_locator = (By.CSS_SELECTOR,'#form1 > table')
    """定位表格tr"""
    tr_locator = (By.TAG_NAME,'tr')
    """定位td"""
    td_locator = (By.TAG_NAME,'td')
    """定位【新建客户】按钮"""
    new_client_locator = (By.CSS_SELECTOR,'body > div.container > div.row > div:nth-child(1) > div > a')
    """客户名称输入框定位"""
    client_locator = (By.ID,'name')
    """【保存】按钮定位"""
    submit_locator = (By.NAME,'submit')
    """定位【查看】"""
    check_locator = (By.LINK_TEXT,'查看')
    """定位【修改】"""
    alter_locator = (By.LINK_TEXT,'修改')
    """定位【编辑】按钮"""
    compile_locator = (By.LINK_TEXT,'编辑')
    """定位【返回】按钮"""
    back_locator = (By.CSS_SELECTOR,'input[value="返回"]')


    """断言客户名称定位"""
    assert_locator = (By.XPATH,'//*[@id="form1"]/table/tbody/tr[1]/td[3]/a/span')

    def click_new_client(self):  #点击新建客户按钮
        hp = HomePage(self.driver)
        hp.click_client()
        self.find_element(self.new_client_locator).click()

    def input_client(self,clientname):  #输入客户名
        self.find_element(self.client_locator).clear()
        sleep(1)
        self.find_element(self.client_locator).send_keys(clientname)

    def click_submit(self):  #点击保存
        self.find_element(self.submit_locator).click()

    def click_check(self,clientname1):   #点击查看
        element = self.find_element(self.table_locator)
        tr_list = self.find_elements(self.tr_locator,element)[2:]
        for tr in tr_list:
            td_list = self.find_elements(self.td_locator,tr)
            print(td_list[2].text)
            if td_list[2].text == clientname1:
                td_list[0].find_element(By.CSS_SELECTOR,'#form1 > table > tbody > tr:nth-child(1) > td:nth-child(1) > input').click()




    def click_alter(self):    #点击修改
        self.find_element(self.alter_locator).click()

    def assert_text(self):  #获取断言客户名称文本
        return (self.find_element(self.assert_locator).text).strip()

    def add_client(self,clientname,clientname1): #客户流程：新建 - 查看 - 修改 - 编辑 - 返回 - 删除
        self.click_new_client()    #点击新建客户
        sleep(1)
        self.input_client(clientname)  #输入客户名称
        sleep(1)
        self.click_submit()   #点击【保存】
        sleep(1)
        self.click_check(clientname1)    #点击【查看】
        sleep(10)
        # self.click_alter()    #点击【修改】
        # sleep(1)
        # self.input_client('北京东兴阳工程技术有限公司')  #修改信息
        # sleep(1)
        # self.click_submit()   #点击确定
        # sleep(1)


