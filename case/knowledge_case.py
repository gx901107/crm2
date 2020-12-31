# -*- coding: utf-8 -*-
# @Time : 2020/12/30 12:15
# @Author : nichao
# @Email : 530504026@qq.com
# @File : knowledge_case.py
# @Project : crm2
from time import sleep
from page.knowledge_page import KnowledgePage
from page.home_page  import HomePage
from model.ncread_datas import read_data_excel
import unittest
from page.login_page import LoginPage
from model.browser import chrome
class KnowledgeCase(unittest.TestCase):
    kntitle,kncontent,newtitle,knkeyword,expected=read_data_excel('addkno')[0]
    def setUp(self) -> None:
        self.driver = chrome()
        lp = LoginPage(self.driver)
        lp.login('admin', '123456')
    def test_knowledge(self):
        hp=HomePage(self.driver)
        hp.more_element()#点击更多
        sleep(1)
        hp.knowlede_element()#点击知识
        kp=KnowledgePage(self.driver)#实例化KnowledgePage
        kp.addknowledge(self.kntitle,self.kncontent)
        sleep(4)
        kp.cheakknowledge(self.newtitle)
        sleep(2)
        kp.searchk_element(self.knkeyword)
        sleep(2)
        kp.deletekonwledge()
        sleep(1)
        self.assertIn(self.expected,kp.assertdlete_knoledge(self.knkeyword),msg='删除失败')
    def tearDown(self) -> None:
        self.driver.quit()