# -*- coding: utf-8 -*-
# @Time : 2020/12/29 9:40
# @Author : 唐涛
# @Email : 2410725336@qq.com
# @File : Business_page.py
# @Project : crm2
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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
    contact_confirmation_locator=(By.CSS_SELECTOR,'body > div:nth-child(18) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(1)')#联系人确认
    business_type_locator=(By.CSS_SELECTOR,'#type')#商机类型
    street_locator=(By.CSS_SELECTOR,'#form1 > table > tbody > tr:nth-child(5) > td:nth-child(2) > input')#街道
    source_business_locator=(By.CSS_SELECTOR,'#origin')#商机来源
    state_locator=(By.CSS_SELECTOR,'#status_id')#状态
    win_rate_locator=(By.ID,'gain_rate')#赢单率
    current_rate_locator=(By.ID,'estimate_price')#预计成交价
    contact_time_locator=(By.ID,'nextstep_time')#下次联系时间
    content_locator=(By.ID,'nextstep')#下次联系内容
    overhead_information_locator=(By.ID,'description')#附加信息
    add_product_locator=(By.CSS_SELECTOR,'#form1 > table > tbody > tr:nth-child(12) > th > input')#添加产品
    product_option_locator=(By.CSS_SELECTOR,'#data > tr > td:nth-child(1) > input.product_id')#添加产品
    product_confirmation_locator=(By.CSS_SELECTOR,'body > div:nth-child(22) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(1) > span')#产品确认
    save_locator=(By.CSS_SELECTOR,'#form1 > table > tfoot > tr > td > input:nth-child(1)')#保存
    screen_locator=(By.CSS_SELECTOR,'#field')#筛选条件
    search_locator=(By.CSS_SELECTOR,'#dosearch')#搜索
    search1_locator=(By.CSS_SELECTOR,'#dosearch') # 搜索
    examine_locator=(By.CSS_SELECTOR,'#form1 > table > tbody > tr > td:nth-child(12) > a:nth-child(1)')#查看
    return_locator=(By.CSS_SELECTOR,'#tab1 > div.container2.top-pad > div > a:nth-child(3)')#返回
    compile_locator=(By.CSS_SELECTOR,'#form1 > table > tbody > tr > td:nth-child(12) > a:nth-child(3)')#编辑
    edit_input_locator=(By.CSS_SELECTOR,'#total_price')#编辑输入
    editors_save_locator=(By.CSS_SELECTOR,'body > div.container > div.row > div > form > table > tfoot > tr > td > input.btn.btn-primary')#保存
    remove_radio_locator=(By.CSS_SELECTOR,'#form1 > table > tbody > tr > td:nth-child(1) > input')#删除单选
    delete_locator=(By.CSS_SELECTOR,'#delete')#删除


    def click_business(self):#点击商机
        self.find_element(self.business_locator).click()
    def click_add_business(self):#添加商机
        self.find_element(self.add_business_locator).click()
    def click_principal(self):#负责人
        self.find_element(self.principal_locator).click()
    def click_single_person(self):#选择负责人
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
    def click_contact_confirmation(self):#联系人确认
        self.find_element(self.customer_confirmation_locator).click()
    def click_business_type(self):#商机类型
        select = Select(self.find_element(self.business_type_locator))
        select.select_by_index(1)
    def input_street(self):#街道
        self.find_element(self.street_locator).send_keys('和平街')
    def click_source_business(self):#商机来源
        select = Select(self.find_element(self.source_business_locator))
        select.select_by_index(1)
    def click_state(self):#状态
        select = Select(self.find_element(self.state_locator))
        select.select_by_index(1)
    def input_win_rate(self):#赢单率
        self.find_element(self.win_rate_locator).send_keys('20')
    def input_current_rate(self):#预计成交价
        self.find_element(self.current_rate_locator).send_keys('100')
    def input_contact_time(self):#下次联系时间
        self.find_element(self.contact_time_locator).send_keys('2020-12-01 16:28')
    def input_content(self):#下次联系内容
        self.find_element(self.content_locator).send_keys('不知道')
    def input_overhead_information(self):#附加信息
        self.find_element(self.overhead_information_locator).send_keys('不知道哦')
    def click_add_product(self):#添加产品
        self.find_element(self.add_product_locator).click()
    def click_product_option(self):#选择产品
        self.find_element(self.product_option_locator).click()
    def click_product_confirmation(self):#产品确认
        self.find_element(self.person_confirmation_locator).click()
    def click_save(self):#保存
        self.find_element(self.state_locator).click()
    def click_screen(self):#筛选条件
        select = Select(self.find_element(self.screen_locator))
        select.select_by_index(1)
    def click_search(self):#搜索
        self.find_element(self.search_locator).click()
    def click_search1(self):#搜索
        self.find_element(self.search1_locator).click()
    def click_examine(self):#查看
        self.find_element(self.examine_locator).click()
    def click_return(self):#返回
        self.find_element(self.return_locator).click()
    def click_compile(self):#编辑
        self.find_element(self.compile_locator).click()
    def input_edit_input(self):#编辑输入
        self.find_element(self.input_edit_input()).send_keys('200')
    def click_editors_save(self):#保存
        self.find_element(self.editors_save_locator).click()
    def click_remove_radio(self):#删除单选
        self.find_element(self.remove_radio_locator).click()
    def click_delete(self):#删除
        self.find_element(self.delete_locator).click()
        self.driver.switch_to.alert.accept()

    def business(self):
        self.click_business()#商机
        self.click_add_business()#添加商机
        self.click_principal()#负责人
        self.click_single_person()#选择负责人
        self.click_person_confirmation()#负责人确认
        self.click_client()#客户
        self.click_customer_radio()#客户单选
        self.click_customer_confirmation()#客户确认
        self.input_amount_business()#商机金额
        self.input_business_name()#商机名
        self.click_contacts()#联系人
        self.click_contact_list()#联系人单选
        self.click_contact_confirmation()#联系人确认
        self.click_business_type()#商机类型
        self.input_street()#街道
        self.click_source_business()#商机来源
        self.click_state()#状态
        self.input_win_rate()#赢单率
        self.input_current_rate()#预计成交价
        self.input_contact_time()#下次联系时间
        self.input_content()#下次联系内容
        self.input_overhead_information()#附加信息
        self.click_add_product()#添加产品
        self.click_product_option()#选择产品
        self.click_product_confirmation()#产品确认
        self.click_save()#保存
        self.click_screen()#筛选条件
        self.click_search()#搜素
        self.click_search1()#搜素
        self.click_examine()#查看
        self.click_return()#返回
        self.click_compile()#编辑
        self.input_edit_input()#编辑输入
        self.click_editors_save()#保存
        self.click_remove_radio()#删除单选
        self.click_delete()#删除




































































