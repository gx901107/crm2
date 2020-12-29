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


class OrganizationPage(BasePage):
    origanization_locator2 = (By.LINK_TEXT, '组织架构')  # 进入组织架构之后的组织架构定位器
    huabei_locator = (By.XPATH, '//*[@id="browser"]/li[2]/ul/li[2]/ul/li[2]/span')  # 华北销售部定位器
    alterpartname_locator = (By.XPATH, '//*[@id="department_edit"]/div[1]/div/input')  # 编辑部门名称定位器
    alter_locator = (By.LINK_TEXT, '修改')  # 编辑部门定位器
    alterbutton_locator = (
        By.CSS_SELECTOR, 'body > div:nth-child(13) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix >'
                         ' div > button:nth-child(1) > span')  # 编辑确定按钮定位器
    shichang_locator = (By.XPATH, '//*[@id="browser"]/li[2]/ul/li[2]/ul/li[1]/span')  # 卡卡罗特办公室下的市场部定位器
    delete_locator = (By.LINK_TEXT, '删除')  # 删除部门定位器
    salesspecialist_locator = (By.XPATH, '//*[@id="browser"]/li/ul/li[3]/ul/li[2]/ul/li/ul/li/span')  # 销售专员岗位定位器
    relations_locator = (By.LINK_TEXT, '上下级关系图')  # 上下关系图定位器
    alterrole_locator = (By.LINK_TEXT, '修改')  # 编辑岗位定位器
    altername_locator = (By.ID, 'name')  # 岗位名称输入框
    alterrolebutton_locator = (By.XPATH, '/html/body/div[11]/div[3]/div/button[1]')  # 编辑岗位确定按钮定位器
    ssleader_locator = (
        By.CSS_SELECTOR,
        '#browser > li > ul > li.collapsable > ul > li:nth-child(2) > ul > li > ul > li > span')  # 销售专员编辑后的定位器
    deletrrole_locator = (By.LINK_TEXT, '删除')  # 岗位删除定位器
    """搜索员工定位器"""
    usermanagement_locator = (By.LINK_TEXT, '用户管理')  # 用户管理的定位器
    searchuser_locator = (By.CSS_SELECTOR, '#user_form > div:nth-child(1) > ul > li > ul > li > a')  # 按类别查找的定位器
    user_locator = (By.LINK_TEXT, '员工')

    def origanization_element(self):
        """组织架构中的组织架构元素"""
        self.find_element(self.origanization_locator2).click()

    def alterbutton_element(self):
        """编辑部门确定按钮"""
        self.find_element(self.alterrolebutton_locator).click()

    def alterpartname_element(self, newpartname):
        """编辑部门名称方法"""
        self.find_element(self.alterpartname_locator).clear()
        sleep(1)
        self.find_element(self.alterpartname_locator).send_keys(newpartname)
        sleep(3)

    def moveto_element(self):
        """鼠标悬浮点击修改"""
        ActionChains(self.driver).move_to_element(self.find_element(self.huabei_locator)).perform()
        sleep(3)
        self.find_element(self.alter_locator).click()
        sleep(6)
    def alterrole(self,newpartname):
        self.origanization_element()
        sleep(2)
        self.moveto_element()
        sleep(1)
        self.alterpartname_element(newpartname)
    """""删除部门"""
    def moveto_delete(self):
        """删除部门"""
        ActionChains(self.driver).move_to_element(self.find_element(self.shichang_locator)).perform()
        sleep(3)
        self.find_element(self.delete_locator).click()
        sleep(3)
        self.switch_dissmiss()
        sleep(2)
        self.find_element(self.delete_locator).click()
        self.switch_to()
    """编辑岗位"""