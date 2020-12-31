# -*- coding: utf-8 -*-
# @Time : 2020/12/29 22:11
# @Author : nichao
# @Email : 530504026@qq.com
# @File : organization1_page.py
# @Project : crm2
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from page.home_page import HomePage
from selenium.webdriver.support.select import Select
from page.base_page import BasePage


class OrPage(BasePage):
    """添加部门相关定位器"""
    adddepartment_locator = (By.ID, 'add_department')  # 添加部门的定位器
    departmentname_locator = (By.ID, 'name')  # 部门名称定位器
    uperiordepartment_locator = (By.NAME, 'parent_id')  # 上级部门的选择定位器
    departmentnamedescription_locator = (
        By.CSS_SELECTOR, '#department_add > div:nth-child(3) > div > textarea')  # 部门描述定位器
    confirm_locator = (By.XPATH, '/html/body/div[8]/div[3]/div/button[1]/span')  # 确定按钮
    """添加岗位定位器"""

    addrole_locator = (By.ID, 'add_role')  # 添加岗位定位器
    rolename_locator = (By.NAME, 'name')  # 岗位名称定位器
    fordepartment_locator = (By.NAME, 'department_id')  # 所属部门定位器
    parent_locator = (By.NAME, 'parent_id')  # 上级部门定位器
    roledescription_locator = (By.CSS_SELECTOR, '#role_add > div:nth-child(4) > div > textarea')  # 部门描述定位器
    roleconfirm_locator = (By.XPATH, '/html/body/div[9]/div[3]/div/button[1]/span')  # 添加岗位确定按钮定位器
    """查看和编辑员工信息"""
    wuser_locator = (By.CSS_SELECTOR, '#tab1 > table > thead > tr > td > p > a:nth-child(3)')  # 查看中的编辑定位器
    wemail_locator = (By.NAME, 'email')  # 邮箱的定位器
    wphone_locator = (By.NAME, 'telephone')  # 电话的定位器
    wuserconfirm_locator = (By.CSS_SELECTOR, 'body > div.container > div.row > div:nth-child(2) >'
                                             ' form > table > tfoot > tr > td:nth-child(2) > input.btn.btn-primary')  # 编辑员工信息保存按钮
    usertable_locator = (By.CSS_SELECTOR, '#user_form > div:nth-child(2) > table > tbody')  # 用户列表tbody
    tr_locator = (By.TAG_NAME, 'tr')
    td_locator = (By.TAG_NAME, 'td')
    a_locator = (By.TAG_NAME, 'a')
    assert_locator = (By.CSS_SELECTOR, 'body > div.container > div.row > div:nth-child(1) > div')  # 断言定位器

    def adddepartment_element(self):
        """"点击添加部门"""
        self.find_element(self.adddepartment_locator).click()

    def departmentname_element(self, departmentname):
        """输入部门"""
        self.find_element(self.departmentname_locator).send_keys(departmentname)

    def uperiordepartment_element(self, index_number):
        """选择上一级部门"""
        Select(self.find_element(self.uperiordepartment_locator)).select_by_index(int(index_number))

    def departmentnamedescription_element(self, departmentdescription):
        """岗位描述"""
        self.find_element(self.departmentnamedescription_locator).send_keys(departmentdescription)

    def confirm_element(self):
        """"点击添加部门确定按钮"""
        self.find_element(self.confirm_locator).click()  # 点击确定按钮

    def add_departmentnamedescription(self, departmentname, index_number, departmentdescription):
        self.adddepartment_element()
        sleep(2)
        self.departmentname_element(departmentname)
        sleep(1)
        self.uperiordepartment_element(int(index_number))
        sleep(1)
        self.departmentnamedescription_element(departmentdescription)
        sleep(1)
        self.confirm_element()

    """"添加岗位"""

    def addrole_element(self):
        """点击添加岗位"""
        self.find_element(self.addrole_locator).click()

    def rolename_element(self, rolename):
        """添加岗位名称"""
        self.find_element(self.rolename_locator).send_keys(rolename)

    def fordepartment_elememt(self, branch_id):
        """选择所属部门"""
        return Select(self.find_element(self.fordepartment_locator)).select_by_index(int(branch_id))

    def parent_element(self, superiorposition_id):
        """选择上级岗位"""
        return Select(self.find_element(self.parent_locator)).select_by_index(int(superiorposition_id))

    def roledescription_element(self, roledescription):
        """填写岗位描述"""
        self.find_element(self.roledescription_locator).send_keys(roledescription)

    def roleconfirm_elememt(self):
        """点击添加岗位确定按钮"""
        self.find_element(self.roleconfirm_locator).click()

    def add_role(self, rolename, branch_id, superiorposition_id, roledescription):
        """添加岗位聚合函数"""
        self.addrole_element()  # 点击添加岗位
        sleep(3)
        self.rolename_element(rolename)  # 添加岗位名称
        sleep(1)
        self.fordepartment_elememt(int(branch_id))  # 选择所属部门
        sleep(1)
        self.parent_element(int(superiorposition_id))  # 选择上级岗位
        sleep(1)
        self.roledescription_element(roledescription)  # 填写岗位描述
        sleep(1)
        self.roleconfirm_elememt()  # 点击添加岗位确定按钮

        """查看和编辑员工信息"""

    def wemail_element(self, email):
        """编辑员工邮箱信息"""
        self.find_element(self.wemail_locator).clear()
        self.find_element(self.wemail_locator).send_keys(email)

    def wphone_element(self, phone):
        """编辑手机信息"""
        self.find_element(self.wphone_locator).clear()
        self.find_element(self.wphone_locator).send_keys(int(phone))

    def wuserconfirm_element(self):
        """点击编辑员工确定按钮"""
        self.find_element(self.wuserconfirm_locator).click()

    def wuser_element(self):
        """点击查看中的编辑"""
        self.find_element(self.wuser_locator).click()

    def cheakandalter(self,email,phone):
        """查看和编辑员工"""
        userdepartment_element = self.find_element(self.usertable_locator)
        tr_list = self.find_elements(self.tr_locator, userdepartment_element)
        for tr in tr_list:
            td_list = self.find_elements(self.td_locator, tr)
            if td_list[1].text.strip() == "小杨":
                print(td_list)
                self.find_elements(self.a_locator, td_list[7])[0].click()
                sleep(3)
                self.wuser_element()
                sleep(1)
                self.wemail_element(email)
                sleep(1)
                self.wphone_element(int(phone))
                sleep(1)
                self.wuserconfirm_element()
                break

    def assert_elment(self):
        return self.find_element(self.assert_locator).text.split('\n')[1]


