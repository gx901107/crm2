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
    check_locator = (By.LINK_TEXT, '查看')
    """定位修改"""
    amend_locator = (By.LINK_TEXT, '修改')
    """定位转换"""
    change_locator = (By.LINK_TEXT, '转换')
    """定位客户名称"""
    client_locator = (By.ID, 'name')
    """定位保存按钮"""
    submit_locator = (By.NAME, 'submit')
    """断言联系人姓名"""
    assert_locator = (By.CSS_SELECTOR, 'body > div.container > div.alert.alert-success')
    """定位线索列表表格"""
    table_locator = (By.CSS_SELECTOR, '#form1 > table')
    """定位表格tr标签"""
    tr_locator = (By.TAG_NAME, 'tr')
    """定位td标签"""
    td_locator = (By.TAG_NAME, 'td')
    """定位a标签"""
    a_locator = (By.TAG_NAME, 'a')
    """选择框定位"""
    select_locator = (By.CSS_SELECTOR, '#form1 > table > tbody > tr:nth-child(1) > td:nth-child(1) > input')
    """批量操作"""
    batch_operation_locator = (By.CSS_SELECTOR, 'body > div.container > div.row > div:nth-child(1) > ul > li:nth-child(1) > div > a')
    """批量删除"""
    batch_remove_locator = (By.LINK_TEXT, '批量删除')
    """回收站"""
    recycle_bin_locator = (By.CSS_SELECTOR,'body > div.container > p > a:nth-child(17)')

    def click_new_clue(self):  # 点击【新建线索】
        hp = HomePage(self.driver)
        hp.click_clue()
        self.find_element(self.new_clue_locator).click()

    def input_linkman(self, linkman):  # 输入联系人姓名
        self.find_element(self.linkman_locator).clear()
        self.find_element(self.linkman_locator).send_keys(linkman)

    def click_sbmit(self):  # 点击【保存】
        self.find_element(self.sbmit_locator).click()

    def click_check(self,linkman):  # 点击【查看】
        element = self.find_element(self.table_locator)
        tr_list = self.find_elements(self.tr_locator, element)[2:]
        for tr in tr_list:
            td_list = self.find_elements(self.td_locator, tr)

            if td_list[2].text == linkman:
                self.find_elements(self.a_locator, td_list[11])[0].click()
                break
    def click_amend(self):  # 点击【修改】
        self.find_element(self.amend_locator).click()

    def click_change(self,linkman1):  # 点击转换
        element = self.find_element(self.table_locator)
        tr_list = self.find_elements(self.tr_locator, element)[2:]
        for tr in tr_list:
            td_list = self.find_elements(self.td_locator, tr)

            if td_list[2].text == linkman1:
                self.find_elements(self.a_locator, td_list[11])[1].click()
                break

    def input_client(self, clientname):  # 输入客户名称
        self.find_element(self.client_locator).send_keys(clientname)

    def click_submit(self):  # 点击保存
        self.find_element(self.submit_locator).click()

    def assert_text(self):  # 获取断言文本
        txt = self.find_element(self.assert_locator).text.strip()
        return txt.splitlines()[1]

    def click_select(self, client):  # 勾选可选（为删除做准备）
        element = self.find_element(self.table_locator)
        tr_list = self.find_elements(self.tr_locator, element)[2:]
        for tr in tr_list:
            td_list = self.find_elements(self.td_locator, tr)
            if td_list[2].text == client:
                self.find_element(self.select_locator, td_list[0]).click()
                break
    def click_batch_operation(self):  #点击批量操作 - 删除
        self.find_element(self.batch_operation_locator).click()
        sleep(1)
        self.find_element(self.batch_remove_locator).click()

    def click_recycle_bin(self):   #点击回收站
        self.find_element(self.recycle_bin_locator).click()


    def add_clue(self, linkman, linkman1, client):  # 添加线索 - 查看 - 修改 - 转换 - 保存
        sleep(2)
        self.click_new_clue()  # 点击【添加线索】
        sleep(2)
        self.input_linkman(linkman)  # 输入联系人（添加线索）
        self.click_sbmit()  # 点击【提交】
        sleep(1)
        self.click_check(linkman)  # 点击【查看】
        sleep(1)
        self.click_amend()  # 点击【修改】（线索详情页面）
        sleep(1)
        self.input_linkman(linkman1)  # 修改联系人名字
        sleep(1)
        self.click_sbmit()  # 点击【提交】
        sleep(1)
        self.click_change(linkman1)  # 点击【转换】
        sleep(1)
        self.input_client(client)  # 输入客户名
        sleep(1)
        self.click_submit()  # 点击【保存】

    def clear_data(self,client):   #清除数据
        hp = HomePage(self.driver)
        hp.click_clue()
        self.click_select(client)  #勾选匹配的联系人
        sleep(1)
        self.click_batch_operation()  #删除
        self.switch_to()
        sleep(1)
        self.click_recycle_bin()  #点击【回收站】
        sleep(1)
        self.click_select(client)  #勾选匹配的联系人
        sleep(1)
        self.click_batch_operation()  #删除
        sleep(1)
        self.switch_to()
        sleep(1)


