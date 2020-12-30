# -*- coding: utf-8 -*-
# @Time : 2020/12/29 14:26
# @Author : nichao
# @Email : 530504026@qq.com
# @File : organization_page.py
# @Project : crm2
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from page.home_page import HomePage

class OrganizationPage(BasePage):
    origanization_locator2 = (By.LINK_TEXT, '组织架构')  # 进入组织架构之后的组织架构定位器
    huabei_locator = (By.XPATH, '//*[@id="browser"]/li[2]/ul/li[2]/ul/li[2]/span')  # 华北销售部定位器
    alterpartname_locator = (By.XPATH, '//*[@id="department_edit"]/div[1]/div/input')  # 编辑部门名称定位器
    alter_locator = (By.LINK_TEXT, '修改')  # 编辑部门定位器
    alterbutton_locator = (
        By.CSS_SELECTOR, 'body > div:nth-child(13) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix >'
                         ' div > button:nth-child(1) > span')  # 编辑部门确定按钮定位器
    shichang_locator = (By.XPATH, '//*[@id="browser"]/li[2]/ul/li[2]/ul/li[1]/span')  # 卡卡罗特办公室下的市场部定位器
    delete_locator = (By.LINK_TEXT, '删除')  # 删除部门定位器
    salesspecialist_locator = (By.XPATH, '//*[@id="browser"]/li/ul/li[3]/ul/li[2]/ul/li/ul/li/span')  # 编辑销售专员岗位定位器
    relations_locator = (By.LINK_TEXT, '上下级关系图')  # 上下关系图定位器
    alterrole_locator = (By.LINK_TEXT, '修改')  # 编辑岗位定位器
    altername_locator = (By.ID, 'name')  # 岗位名称输入框
    alterrolebutton_locator=(By.XPATH,'/html/body/div[11]/div[3]/div/button[1]')  # 编辑岗位确定按钮定位器
    ssleader_locator = (
        By.CSS_SELECTOR,
        '#browser > li > ul > li.collapsable > ul > li:nth-child(2) > ul > li > ul > li > span')  # 销售专员编辑后的定位器
    deletrrole_locator = (By.LINK_TEXT, '删除')  # 岗位删除定位器
    """搜索员工定位器"""
    usermanagement_locator = (By.LINK_TEXT, '用户管理')  # 用户管理的定位器
    searchuser_locator = (By.CSS_SELECTOR, '#user_form > div:nth-child(1) > ul > li > ul > li > a')  # 按类别查找的定位器
    user_locator = (By.LINK_TEXT, '员工')
    aserttable_locator = (By.CSS_SELECTOR, '#user_form > div:nth-child(2) > table > tbody')#断言表单
    tr_locator = (By.TAG_NAME, 'tr')
    td_locator = (By.TAG_NAME, 'td')

    def origanization_element(self):
        """点击组织架构中的组织架构"""
        self.find_element(self.origanization_locator2).click()

    def alterbutton_element(self):
        """编辑部门确定按钮"""
        self.find_element(self.alterbutton_locator).click()

    def alterpartname_element(self):
        """编辑部门名称方法"""
        self.find_element(self.alterpartname_locator).clear()
        sleep(3)
        self.find_element(self.alterpartname_locator).send_keys('西南销售部')
        sleep(3)

    def moveto_element(self):
        """鼠标悬浮点击修改"""
        ActionChains(self.driver).move_to_element(self.find_element(self.huabei_locator)).perform()
        sleep(3)
        self.find_element(self.alter_locator).click()
        sleep(6)

    def alterrole(self):
        """编辑部门名称"""
        self.moveto_element()
        sleep(2)
        self.alterpartname_element()
        sleep(2)
        self.alterbutton_element()

    """""删除部门"""

    def moveto_delete(self):
        """删除卡卡罗特办公室下的市场部门"""
        ActionChains(self.driver).move_to_element(self.find_element(self.shichang_locator)).perform()
        sleep(3)
        self.find_element(self.delete_locator).click()
        sleep(3)
        self.switch_dissmiss()
        sleep(2)
        self.find_element(self.delete_locator).click()
        self.switch_to()

    """编辑岗位"""

    def relations_element(self):
        """点击【上下级关系图】"""
        self.find_element(self.relations_locator).click()

    def altername_element(self):
        """编辑岗位名称（讲专员改为销售小小组长）"""
        self.find_element(self.altername_locator).clear()  # 清除输入框内容
        self.find_element(self.altername_locator).send_keys('销售小小组长')

    def alterrolebutton_element(self):
        """点击编辑岗位保存按钮"""
        self.find_element(self.alterrolebutton_locator).click()

    def moveto_alterrole(self):
        """点击销售专员岗位的编辑"""
        ActionChains(self.driver).move_to_element(self.find_element(self.salesspecialist_locator)).perform()
        self.find_element(self.alterrole_locator).click()  # 点击编辑

    def alter_role(self):
        """编辑岗位聚合函数"""
        self.relations_element()  # 点击上下级关系图
        sleep(1)
        self.moveto_alterrole()
        sleep(1)
        self.altername_element()
        sleep(1)
        self.alterrolebutton_element()
        sleep(1)
        self.switch_to()
        sleep(1)
        self.driver.refresh()

    """""删除岗位"""

    def roledelete_element(self):
        ActionChains(self.driver).move_to_element(self.find_element(self.ssleader_locator)).perform()
        self.find_element(self.deletrrole_locator).click()
        sleep(2)
        self.switch_dissmiss()
        sleep(2)
        self.find_element(self.deletrrole_locator).click()
        sleep(3)
        self.switch_to()

    """"搜索员工"""

    def usermanagement_element(self):
        """点击用户管理"""
        self.find_element(self.usermanagement_locator).click()

    def searchuser_element(self):
        """点击按类别查找"""
        self.find_element(self.searchuser_locator).click()  # 点击按类别查找

    def user_element(self):
        """"点击按员工方式查找"""
        self.find_element(self.user_locator).click()  # 点击员工

    def searchuser(self):
        """搜索员工聚合函数"""
        self.usermanagement_element()
        sleep(2)
        self.searchuser_element()
        sleep(1)
        self.user_element()
    def aserttable_element(self):
        tr_list= self.find_element(self.aserttable_locator).find_elements(*self.tr_locator)
        lit=[]
        for tr in tr_list:
            td_list = tr.find_elements(*self.td_locator)
            lit.append(td_list[1].text)
        return len(lit)
