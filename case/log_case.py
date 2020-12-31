# -*- coding: utf-8 -*-
# @Time : 2020/12/30 11:06
# @Author : nichao
# @Email : 530504026@qq.com
# @File : log_case.py
# @Project : crm2
from time import sleep
from page.home_page import HomePage
from page.log_page import LogPage
from case.base_case import BaseCase
class Log(BaseCase):

    def test_log(self):
        hp=HomePage(self.driver)
        hp.more_element()
        sleep(2)
        hp.log_element()
        lp=LogPage(self.driver)
        lp.addlog()#新建日志
        sleep(2)
        lp.cheak_log()#查看日志
        sleep(2)
        lp.alter_log()#编辑日志
        sleep(2)
        lp.search_log()#搜索日志
        sleep(2)
        lp.delete_log()#删除日志
        sleep(2)
        self.assertIn('----暂无数据！----',lp.assert_delete(),msg='删除失败')