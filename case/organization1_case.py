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
    
    email,phone=datas[0]
    def test_organ(self):
        hp = HomePage(self.driver)
        hp.head_portrait()
        sleep(2)
        hp.organizational_structure_submit()
        sleep(2)
        op = OrPage(self.driver)
        op.add_departmentnamedescription()
        sleep(3)
        op.add_role()
        sleep(3)
        op.cheakandalter()
        self.assertEqual('员工信息修改成功！', op.assert_elment(), msg='编辑失败')
