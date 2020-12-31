# -*- coding: utf-8 -*-
# @Time : 2020/12/29 20:47
# @Author : nichao
# @Email : 530504026@qq.com
# @File : organization_case.py
# @Project : crm2
from page.home_page import HomePage
from time import sleep
from page.organization_page import OrganizationPage
from model.ncread_datas import read_data_excel
from page.organization1_page import OrPage
import unittest
from page.login_page import LoginPage
from model.browser import chrome


class Organization(unittest.TestCase):
    newpartname, newrolename, expected = read_data_excel('editorgan')[0]

    def setUp(self) -> None:
        self.driver = chrome()
        lp = LoginPage(self.driver)
        lp.login('admin', '123456')

    def test_organization(self):
        hp = HomePage(self.driver)
        hp.head_portrait()
        sleep(2)
        hp.organizational_structure_submit()
        sleep(2)
        op = OrganizationPage(self.driver)
        op.origanization_element()
        sleep(2)
        op.alterrole(self.newpartname)  # 编辑部门
        sleep(2)
        op.alterrole('华北销售部')
        sleep(2)
        op.moveto_delete()  # 删除部门
        op1 = OrPage(self.driver)
        op1.add_departmentnamedescription('市场部', 3, '营销工作')
        sleep(2)
        op.alter_role(self.newrolename)  # 编辑岗位
        sleep(2)
        op.roledelete_element()
        sleep(2)
        op1.add_role('销售专员', 6, 7, '负责销售事宜')
        sleep(2)
        op.searchuser()
        sleep(2)
        self.assertEqual(int(self.expected), op.aserttable_element(), msg='测试不通过')
    def tearDown(self) -> None:
        self.driver.quit()
