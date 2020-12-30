# -*- coding: utf-8 -*-
# @Time : 2020/12/12 19:34
# @Author : fcj11
# @Email : yangfit@126.com
# @File : clue_page.py
# @Project : crm自动化测试
from time import sleep
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.home_page import HomePage



class NEWClue(BasePage):
    """新建线索按钮定位"""
    new_clue_locator = (By.CSS_SELECTOR, 'body > div.container > div.row > div:nth-child(1) > div > a')
    """联系人输入框定位"""
    linkman_locator = (By.ID, 'contacts_name')
    """保存按钮定位"""
    sbmit_locator = (By.CSS_SELECTOR, '#form1 > table > tfoot > tr > td > input:nth-child(1)')
    """定位查看"""
    check_locator = (By.LINK_TEXT,'查看')
    """定位修改"""
    amend_locator = (By.LINK_TEXT,'修改')
    """定位转换"""
    change_locator = (By.LINK_TEXT,'转换')
    """定位客户名称"""
    client_locator = (By.ID, 'name')
    """定位保存按钮"""
    submit_locator = (By.NAME, 'submit')
    """断言联系人姓名"""
    assert_locator = (By.CSS_SELECTOR,'body > div.container > div.alert.alert-success')

    def click_new_clue(self):  #点击【新建线索】
        hp=HomePage(self.driver)
        hp.click_clue()
        self.find_element(self.new_clue_locator).click()

    def input_linkman(self,linkman):  #输入联系人姓名
        self.find_element(self.linkman_locator).clear()
        self.find_element(self.linkman_locator).send_keys(linkman)

    def click_sbmit(self):   #点击【保存】
        self.find_element(self.sbmit_locator).click()

    def click_check(self):  #点击【查看】
        self.find_element(self.check_locator).click()

    def click_amend(self):   #点击【修改】
        self.find_element(self.amend_locator).click()

    def click_change(self):   #点击转换
        self.find_element(self.change_locator).click()

    def input_client(self,clientname):  #输入客户名称
        self.find_element(self.client_locator).send_keys(clientname)

    def click_submit(self):  #点击保存
        self.find_element(self.submit_locator).click()

    def assert_text(self):  #获取断言文本
        txt = self.find_element(self.assert_locator).text.strip()
        return  txt.splitlines()[1]


    def add_clue(self,linkman,linkman1,client):   #添加线索 - 查看 - 修改 -
        sleep(2)
        self.click_new_clue()   #点击【添加线索】
        sleep(2)
        self.input_linkman(linkman)  #输入联系人（添加线索）
        self.click_sbmit()  #点击【提交】
        sleep(1)
        self.click_check()  #点击【查看】
        sleep(1)
        self.click_amend()  #点击【修改】（线索详情页面）
        sleep(1)
        self.input_linkman(linkman1)  #修改联系人名字
        sleep(1)
        self.click_sbmit()  #点击【提交】
        sleep(1)
        self.click_change()  #点击【转换】
        sleep(1)
        self.input_client(client)  #输入客户名
        sleep(1)
        self.click_submit()  #点击【保存】

