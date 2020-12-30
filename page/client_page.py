# -*- coding: utf-8 -*-
# @Time : 2020/12/12 22:08
# @Author : fcj11
# @Email : yangfit@126.com
# @File : client.py
# @Project : crm自动化测试
from time import sleep
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.home_page import HomePage


class NewClient(BasePage):
    """定位器"""
    """定位客户列表表格"""
    table_locator = (By.CSS_SELECTOR, '#form1 > table')
    """定位表格tr标签"""
    tr_locator = (By.TAG_NAME, 'tr')
    """定位td标签"""
    td_locator = (By.TAG_NAME, 'td')
    """定位a标签"""
    a_locator = (By.TAG_NAME, 'a')
    """定位【新建客户】按钮"""
    new_client_locator = (By.CSS_SELECTOR, 'body > div.container > div.row > div:nth-child(1) > div > a')
    """客户名称输入框定位"""
    client_locator = (By.ID, 'name')
    """【保存】按钮定位"""
    submit_locator = (By.NAME, 'submit')
    """定位【查看】"""
    check_locator = (By.LINK_TEXT, '查看')
    """定位【修改】"""
    alter_locator = (By.LINK_TEXT, '修改')
    """定位【编辑】按钮"""
    compile_locator = (By.LINK_TEXT, '编辑')
    """定位【返回】按钮"""
    back_locator = (By.CSS_SELECTOR, 'input[value="返回"]')
    """选择框定位"""
    select_locator = (By.CSS_SELECTOR, '#form1 > table > tbody > tr > td:nth-child(1) > input')
    """批量操作"""
    batch_operation_locator = (By.CSS_SELECTOR, 'body > div.container > div.row > div:nth-child(1) > ul > div > a')
    """批量删除"""
    batch_remove_locator = (By.LINK_TEXT, '批量删除')
    """断言客户名称定位"""
    assert_locator = (By.XPATH, '//*[@id="form1"]/table/tbody/tr[1]/td[3]/a/span')

    def click_new_client(self):  # 点击新建客户按钮
        hp = HomePage(self.driver)
        hp.click_client()
        self.find_element(self.new_client_locator).click()

    def input_client(self, clientname):  # 输入客户名
        self.find_element(self.client_locator).send_keys(clientname)

    def click_clear(self):  # 清楚
        self.find_element(self.client_locator).clear()

    def click_submit(self):  # 点击保存
        self.find_element(self.submit_locator).click()

    def click_check(self, clientname1):  # 点击查看
        # self.find_element(self.check_locator).click()
        element = self.find_element(self.table_locator)
        tr_list = self.find_elements(self.tr_locator, element)[2:]
        for tr in tr_list:
            td_list = self.find_elements(self.td_locator, tr)
            # print(td_list[11].text)

            if td_list[2].text == clientname1:
                self.find_elements(self.a_locator, td_list[11])[0].click()
                break

    def click_alter(self):  # 点击修改
        self.find_element(self.alter_locator).click()

    def click_compile(self):  # 点击编辑
        self.find_element(self.compile_locator).click()

    def click_back(self):  # 点击返回
        self.find_element(self.back_locator).click()

    def click_select(self, clientname1):  # 勾选可选（为删除做准备）
        element = self.find_element(self.table_locator)
        tr_list = self.find_elements(self.tr_locator, element)[2:]
        for tr in tr_list:
            td_list = self.find_elements(self.td_locator, tr)
            # print(td_list[2].text)
            if td_list[2].text == clientname1:
                self.find_element(self.select_locator, td_list[0]).click()
                break

    def click_batch_operation(self):  # 点击批量操作
        self.find_element(self.batch_operation_locator).click()

    def click_batch_Remove(self):  # 点击批量删除
        self.find_element(self.batch_remove_locator).click()
        self.switch_to()

    def assert_text(self):  # 获取断言客户名称文本
        return (self.find_element(self.assert_locator).text).strip()

    def add_client(self, clientname, clientname1):  # 客户流程：新建 - 查看 - 修改 - 编辑 - 返回 - 删除
        self.click_new_client()  # 点击新建客户
        sleep(1)
        self.input_client(clientname)  # 输入客户名称
        sleep(1)
        self.click_submit()  # 点击【保存】
        sleep(1)
        self.click_check(clientname)  # 点击【查看】
        sleep(1)
        self.click_alter()  # 点击【修改】
        sleep(1)
        self.click_clear()
        sleep(1)
        self.switch_to()
        self.input_client(clientname1)  # 修改信息
        sleep(1)
        self.click_submit()  # 点击确定
        sleep(1)
        self.click_compile()  # 点击编辑
        sleep(1)
        self.click_back()  # 点击返回
        sleep(1)
        self.click_select(clientname1)  # 勾选选择框
        sleep(1)
        self.click_batch_operation()  # 点击批量操作
        sleep(1)
        self.click_batch_Remove()  # 删除
