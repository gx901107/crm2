# -*- coding: utf-8 -*-
# @Time : 2020/12/12 19:40
# @Author : fcj11
# @Email : yangfit@126.com
# @File : test_case.py
# @Project : crm自动化测试


import unittest
from time import sleep
from case.base_case import BaseCase
from page.clue_page import NEWClue
from page.client_page import NewClient
from model.read_datas import read_login_excel, read_clue_excel, read_client_excel, read_opportunity_excel


class MyTest(BaseCase):

    def test_1(self):
        clue, expected = read_clue_excel()[1]
        nc = NEWClue(self.driver)
        nc.add_clue(clue)
        sleep(2)

        # clue_text = nc.assert_text()
        # self.assertEqual(expected, clue_text, '添加失败')

    # def test_2(self):
    #     client, expected = read_client_excel()[3]
    #     ncl = NewClient(self.driver)
    #     ncl.add_client(client)
    #     sleep(2)
    #
    #     clien_text = ncl.assert_text()
    #     self.assertEqual(client, clien_text, '添加失败')



if __name__ == '__main__':
    unittest.main()
