# -*- coding: utf-8 -*-
# @Time : 2020/12/30 2:09
# @Author : nichao
# @Email : 530504026@qq.com
# @File : log_page.py
# @Project : crm2
from time import sleep

from page.base_page import BasePage
from page.home_page import HomePage
from selenium.webdriver.common.by import By


class LogPage(BasePage):
    createlog_locator = (By.CSS_SELECTOR, 'body > div.container > div.row > div:nth-child(2) > div > a')  # 新建日志定位器
    logtitle_locator = (By.XPATH, '/html/body/div[5]/div[2]/div/form/table/tbody/tr[2]/td[2]/input')  # 日志标题定位器
    monthlog_locator = (By.XPATH, '/html/body/div[5]/div[2]/div/form/table/tbody/tr[3]/td[2]/input[4]')  # 月报定位器
    logsave_locator = (By.XPATH, '/html/body/div[5]/div[2]/div/form/table/tfoot/tr/td[2]/input[1]')  # 添加日志保存定位器
    inputboxiframe_locator = (
        By.XPATH, '/html/body/div[5]/div[2]/div/form/table/tbody/tr[8]/td[2]/div/div[2]/iframe')  # 日志内容输入框iframe
    logcontent_locator = (By.XPATH, '/html/body')  # 日志内容输入框
    logtable_locator = (By.XPATH, '//*[@id="form1"]/table/tbody')  # 日志列表的定位器
    tr_locator = (By.TAG_NAME, 'tr')
    td_locator = (By.TAG_NAME, 'td')
    cheak_locator = (By.CSS_SELECTOR, 'a:nth-child(1)')  # 日志查看按钮
    altre_locator = (By.CSS_SELECTOR, 'a:nth-child(2)')  # 日志编辑按钮
    returepage_locator = (By.LINK_TEXT, '返回上一页')
    altertitle_locator = (By.CSS_SELECTOR,
                          'body > div.container > div.row > div > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > input')  # 编辑日志标题定位器
    altertitlesave_locator = (By.XPATH, '/html/body/div[5]/div[2]/div/form/table/tfoot/tr/td[2]/input[1]')  # 编辑体制保存按钮
    alterreturn_locator = (By.LINK_TEXT, '返回列表页')
    search_locator = (By.ID, 'search')  # 搜索输入框定位器
    searchbutton_locator = (By.CSS_SELECTOR, '#searchForm > ul > li:nth-child(4) > button')  # 搜索按钮定位器
    delietelog_locator = (By.XPATH, '//*[@id="form1"]/table/tbody/tr[1]/td[1]/input')  # 删除第一个日志的定位器
    deletebutton_locator = (By.CSS_SELECTOR, '#delete')  # 删除按钮定位器
    assert_loctor = (By.CSS_SELECTOR, '#form1 > table > tbody > tr > td')  # 断言使用定位器

    def createlog_element(self):
        """点击新建日志"""
        self.find_element(self.createlog_locator).click()

    def logtitle_element(self, addlogtile):
        """输入日志标题"""
        self.find_element(self.logtitle_locator).clear()
        self.find_element(self.logtitle_locator).send_keys(addlogtile)

    def logtype_element(self):
        """选择日志类型为月报"""
        self.find_element(self.monthlog_locator).click()  # 点击月报

    def logcontent_element(self, content):
        self.switchparent_frame()  # 切到上级frame
        self.switch_frame(self.find_element(self.inputboxiframe_locator))  # 切换到文本输入框
        sleep(2)
        self.find_element(self.logcontent_locator).send_keys(content)  # 输入日志内容

    def logsave_element(self):
        """点击新建日志保存按钮"""
        self.switchparent_frame()  # 返回上一级frame
        sleep(3)
        self.find_element(self.logsave_locator).click()
        """查看日志"""
        sleep(3)

    def addlog(self, addlogtile, content):
        """"新建日志聚合函数"""
        self.createlog_element()  # 新建日志
        sleep(3)
        self.logtitle_element(addlogtile)  # 输入日志标题
        sleep(2)
        self.logtype_element()  # 选择日志类型
        sleep(2)
        self.logcontent_element(content)  # 输入日志内容
        sleep(2)
        self.logsave_element()  # 点击保存

    """"查看日志"""

    def returepage(self):
        """查看日志后返回上一页"""
        self.find_element(self.returepage_locator).click()

    def cheak_log(self):
        """查看日志"""
        table_element = self.find_element(self.logtable_locator)
        tr_list = self.find_elements(self.tr_locator, table_element)
        for tr in tr_list:
            td_list = self.find_elements(self.td_locator, tr)
            if td_list[2].text == '2020-12-28 工作日志':
                self.find_element(self.cheak_locator, td_list[6]).click()
                sleep(2)
                self.returepage()
                break

    """编辑日志"""

    def altertitle_element(self, newtitle):
        """编辑日志标题"""
        self.find_element(self.altertitle_locator).clear()
        self.find_element(self.altertitle_locator).send_keys(newtitle)

    def altertitlesave_element(self):
        """点击编辑日志保存按钮"""
        self.find_element(self.altertitlesave_locator).click()

    def alterreturn_element(self):
        """编辑日志页面返回列表"""
        self.find_element(self.alterreturn_locator).click()  # 点击返回列表

    def alter_log(self, newtitle):
        table_element = self.find_element(self.logtable_locator)
        tr_list = self.find_elements(self.tr_locator, table_element)
        sleep(1)
        for tr in tr_list:
            td_list = self.find_elements(self.td_locator, tr)
            if td_list[2].text == '2020-12-28 工作日志':
                sleep(3)
                self.find_element(self.altre_locator, td_list[6]).click()
                sleep(2)
                self.altertitle_element(newtitle)
                sleep(2)
                self.altertitlesave_element()
                sleep(1)
                self.alterreturn_element()
                break

    """搜索"""

    def searchbutton_element(self):
        """点击搜索按钮"""
        self.find_element(self.searchbutton_locator).click()  # 点击搜索按钮

    def searchword_element(self,keyword):
        """输入搜索关键字"""
        self.find_element(self.search_locator).send_keys(keyword)  # 输入关键子

    def search_log(self,keyword):
        """搜索日志聚合函数"""
        self.searchword_element(keyword)
        sleep(3)
        self.searchbutton_element()

    """删除"""

    def delietelog(self):
        """选需要删除的日志"""
        self.find_element(self.delietelog_locator).click()  # 选择需要删除的日志

    def deletebutton_element(self):
        """点击删除按钮"""
        self.find_element(self.deletebutton_locator).click()

    def delete_log(self):
        """删除日志聚合函数"""
        self.delietelog()
        sleep(1)
        self.deletebutton_element()
        sleep(1)
        self.switch_dissmiss()
        sleep(1)
        self.deletebutton_element()
        sleep(1)
        self.switch_to()

    def assert_delete(self,keyword):
        self.search_log(keyword)
        sleep(3)
        return self.find_element(self.assert_loctor).text.strip()
