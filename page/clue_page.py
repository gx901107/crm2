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
    new_clue_locator = (By.CSS_SELECTOR, 'body > div.container > div.row > div:nth-child(1) > div > a')  #新建线索按钮定位
    linkman_locator = (By.ID, 'contacts_name')  #联系人输入框定位
    sbmit_locator = (By.CSS_SELECTOR, '#form1 > table > tfoot > tr > td > input:nth-child(1)')  #保存按钮定位
    assert_locator = (By.XPATH,'//*[@id="form1"]/table/tbody/tr[1]/td[3]/span') #断言联系人姓名

    def click_new_clue(self):  #点击新建线索
        hp=HomePage(self.driver)
        hp.click_clue()
        self.find_element(self.new_clue_locator).click()

    def input_linkman(self,linkman):  #输入联系人姓名
        self.find_element(self.linkman_locator).send_keys(linkman)

    def click_sbmit(self):   #点击保存
        self.find_element(self.sbmit_locator).click()

    def assert_text(self):
        return self.find_element(self.assert_locator).text

    def add_clue(self,linkman):   #添加线索过程
        sleep(2)
        self.click_new_clue()
        sleep(2)
        self.input_linkman(linkman)
        self.click_sbmit()
