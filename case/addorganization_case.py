# -*- coding: utf-8 -*-
# @Time : 2020/12/29 23:49
# @Author : nichao
# @Email : 530504026@qq.com
# @File : organization1_case.py
# @Project : crm2
from time import sleep
from case.base_case import BaseCase
from page.home_page import HomePage
from page.organization1_page import OrPage
from model.ncread_datas import read_data_excel


class Organ(BaseCase):
    datas = read_data_excel('addorgan')
    departmentname, index_number, departmentdescription, rolename, branch_id, superiorposition_id, roledescription, email, phone,expected = datas[0]

    def test_organ(self):
        hp = HomePage(self.driver)
        hp.head_portrait()
        sleep(2)
        hp.organizational_structure_submit()
        sleep(2)
        op = OrPage(self.driver)
        op.add_departmentnamedescription(self.departmentname,self.index_number,self.departmentdescription)
        sleep(3)
        op.add_role(self.rolename,self.branch_id,self.superiorposition_id,self.roledescription)
        sleep(3)
        op.cheakandalter(self.email,self.phone)
        self.assertIn(self.expected, op.assert_elment(), msg='编辑失败')
