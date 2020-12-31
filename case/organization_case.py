# -*- coding: utf-8 -*-
# @Time : 2020/12/29 20:47
# @Author : nichao
# @Email : 530504026@qq.com
# @File : organization_case.py
# @Project : crm2
from case.base_case import BaseCase
from page.home_page import HomePage
from time import sleep
from page.organization_page import OrganizationPage
class Organization(BaseCase):
    def test_organization(self,rolename,):
        hp=HomePage(self.driver)
        hp.head_portrait()
        sleep(2)
        hp.organizational_structure_submit()
        sleep(2)
        op=OrganizationPage(self.driver)
        op.origanization_element()
        sleep(2)
        op.alterrole()#编辑部门
        sleep(2)
        op.moveto_delete()#删除部门
        sleep(2)
        op.alter_role()#编辑岗位
        sleep(2)
        op.roledelete_element()
        sleep(2)
        op.searchuser()
        sleep(2)
        self.assertEqual(2,op.aserttable_element(),msg='测试不通过')
