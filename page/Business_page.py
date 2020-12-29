# -*- coding: utf-8 -*-
# @Time : 2020/12/29 9:40
# @Author : 唐涛
# @Email : 2410725336@qq.com
# @File : Business_page.py
# @Project : crm2
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.login_page import LoginPage
from time import sleep
class BusinessPage(BasePage):
    '''商机页面类'''
    #定义定位器
    business_locator=(By.LINK_TEXT,'商机')#商机
    add_business_locator=(By.CLASS_NAME,'btn-primary')#添加商机
    principal_locator=(By.ID,'owner_name')#负责人
    single_person_locator=(By.CSS_SELECTOR,'#d_content > tr:nth-child(1) > td:nth-child(1) > input[type=radio]')#选择负责人
    person_confirmation_locator=(By.XPATH,'/html/body/div[12]/div[3]/div/button[1]/span')#负责人确认
    client_locator=(By.NAME,'customer_name')#客户
    customer_radio_locator=(By.NAME,'customer')#客户单选
    customer_confirmation_locator=(By.XPATH,'/html/body/div[10]/div[3]/div/button[1]/span')#客户确认
    amount_business_locator=(By.NAME,'total_price')#商机金额
    business_name_locator=(By.CSS_SELECTOR,'#name')#商机名
    contacts_locator=(By.NAME,'contacts_name')#联系人
    contact_list_locator=(By.NAME,'contacts')#联系人单选


    def click_business(self):#点击商机
        self.find_element(self.business_locator).click()
    def click_add_business(self):#添加商机
        self.find_element(self.add_business_locator).click()
    def click_principal(self):#负责人
        self.find_element(self.principal_locator).click()
    def click_client(self):#选择负责人
        self.find_element(self.single_person_locator).click()
    def click_person_confirmation(self):#负责人确认
        self.find_element(self.person_confirmation_locator).click()
    def click_client(self):#客户
        self.find_element(self.client_locator).click()
    def click_customer_radio(self):#客户单选
        self.find_element(self.customer_radio_locator).click()
    def click_customer_confirmation(self):#客户确认
        self.find_element(self.customer_confirmation_locator).click()
    def input_amount_business(self):#商机金额
        self.find_element(self.amount_business_locator).send_keys('1234')
    def input_business_name(self):#商机名
        self.find_element(self.business_locator).send_keys('2343245')
    def click_contacts(self):#联系人
        self.find_element(self.contacts_locator).click()
    def click_contact_list(self):#联系人单选
        self.find_element(self.contact_list_locator).click()













