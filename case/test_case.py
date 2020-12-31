# -*- coding: utf-8 -*-
# @Time : 2020/12/12 19:40
# @Author : fcj11
# @Email : yangfit@126.com
# @File : test_case.py
# @Project : crm自动化测试


import unittest
from time import sleep
# from case.base_case import BaseCase
from model.browser import chrome
from page.client_pond_page import NewClientPond
from page.clue_page import NEWClue
from page.client_page import NewClient
from model.read_datas import read_clue_excel, read_client_excel
from page.clue_pond_page import NEWCluePond
from page.login_page import LoginPage


class CrmTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = chrome()
        lp = LoginPage(self.driver)
        lp.login('xiaoyang','123456')


    def test_clue(self):  # 流程：添加线索 - 查看 - 修改 - 转换 - 保存
        linkman, linkman1, client, expected = read_clue_excel('clue')[2]
        nc = NEWClue(self.driver)
        nc.add_clue(linkman, linkman1, client)
        sleep(2)

        """断言"""
        clue_text = nc.assert_text()  # 获取文本【添加客户成功！】
        self.assertEqual(expected, clue_text, '添加客户失败')

        """清除数据"""
        nt = NewClient(self.driver)
        nt.clear_client_data(client)  # 清除数据
        sleep(1)
        nt.clear_recycle_bin(client)  # 清除回收站数据
        sleep(1)

    def test_clue_pond(self):    # 线索池流程：新建线索（放入线索池） - 搜索（线索池） - 修改 - 返回 - 分配
        clientname,expected = read_clue_excel('clue_pond')[2]
        ncp = NEWCluePond(self.driver)
        ncp.clue_pond_flow(clientname)

        """断言"""
        clue_pond_text = ncp.assert_text()  # 获取文本【分配成功！】
        self.assertEqual(expected, clue_pond_text, '添加失败')
        """删除数据"""
        nc = NEWClue(self.driver)
        nc.clear_data(clientname)
        sleep(2)


    #
    def test_client(self):  # 客户流程：新建 - 查看 - 修改 - 编辑 - 返回 - 删除
        clientname, clientname1, expected = read_client_excel('client')[2]
        nc = NewClient(self.driver)
        nc.add_client(clientname, clientname1)
        sleep(1)

        """断言"""
        clien_text = nc.assert_text()  # 获取文本【删除成功！】
        self.assertEqual(expected, clien_text, '删除失败')

        """清数据"""
        nc.clear_recycle_bin(clientname1)

    def test_client_pond(self):   # 客户池流程：新建客户（放入客户池） - 搜索客户 - 编辑客户 -分配 - 确定
        clientname, clientname1, expected = read_client_excel('client_pond')[2]
        ncp = NewClientPond(self.driver)
        ncp.client_pond_flow(clientname, clientname1)
        sleep(1)
        """断言"""
        clien_pond_text = ncp.assert_text()  # 获取文本【分配成功！】
        self.assertEqual(expected, clien_pond_text, '异常')

        """清除数据"""
        nt = NewClient(self.driver)
        nt.clear_client_data(clientname1)  # 清除数据
        sleep(1)
        nt.clear_recycle_bin(clientname1)  # 清除回收站数据
        sleep(1)

    def tearDown(self) -> None:
            self.driver.quit()
if __name__ == '__main__':
    unittest.main()
