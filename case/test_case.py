# -*- coding: utf-8 -*-
# @Time : 2020/12/12 19:40
# @Author : fcj11
# @Email : yangfit@126.com
# @File : test_case.py
# @Project : crm自动化测试


import unittest
from time import sleep
from case.base_case import BaseCase
from page.client_pond_page import NewClientPond
from page.clue_page import NEWClue
from page.client_page import NewClient
from model.read_datas import read_login_excel, read_clue_excel, read_client_excel, read_opportunity_excel
from page.clue_pond_page import NEWCluePond

class CrmTest(BaseCase):

    def test_clue(self):

        linkman,linkman1,client,expected = read_clue_excel()[3]
        nc = NEWClue(self.driver)
        nc.add_clue(linkman,linkman1,client)
        sleep(3)

        clue_text = nc.assert_text()
        self.assertEqual(expected, clue_text, '添加客户失败')

    def test_clue_pond(self):
        client, expected = read_client_excel()[27]
        ncp = NewClientPond(self.driver)
        ncp.client_pond_flow(client,expected)

        sleep(5)
        clien_text = ncp.assert_text()  #获取文本【分配成功！】
        self.assertEqual(client, clien_text, '添加失败')



if __name__ == '__main__':
    unittest.main()
