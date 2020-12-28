# -*- coding: utf-8 -*-
# @Time : 2020/12/12 22:08
# @Author : fcj11
# @Email : yangfit@126.com
# @File : client.py
# @Project : crm自动化测试

from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.home_page import HomePage

class NewClient(BasePage):
    new_client_locator = (By.CSS_SELECTOR,'body > div.container > div.row > div:nth-child(1) > div > a')  #新建客户按钮定位
    client_locator = (By.ID,'name')    #客户名称输入框定位
    submit_locator = (By.NAME,'submit')  #保存按钮定位
    assert_locator = (By.XPATH,'//*[@id="form1"]/table/tbody/tr[1]/td[3]/a/span')  #断言客户名称定位

    def click_new_client(self):  #点击新建客户按钮
        hp = HomePage(self.driver)
        hp.click_client()
        self.find_element(self.new_client_locator).click()


    def input_client(self,clientname):  #输入客户名
        self.find_element(self.client_locator).send_keys(clientname)

    def click_submit(self):  #点击保存
        self.find_element(self.submit_locator).click()

    def assert_text(self):  #获取断言客户名称文本
        return (self.find_element(self.assert_locator).text).strip()

    def add_client(self,clientname):
        self.click_new_client()
        self.input_client(clientname)
        self.click_submit()