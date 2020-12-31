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
from model.ncread_datas import read_data_excel
class Log(BaseCase):
    addlogtile,content,newtitle,keyword,expected=read_data_excel('addlog')[0]
    def test_log(self):
        hp=HomePage(self.driver)
        hp.more_element()
        sleep(2)
        hp.log_element()
        lp=LogPage(self.driver)
        lp.addlog(self.addlogtile,self.content)#新建日志
        sleep(2)
        lp.cheak_log()#查看日志
        sleep(2)
        lp.alter_log(self.newtitle)#编辑日志
        sleep(2)
        lp.search_log(self.keyword)#搜索日志
        sleep(2)
        lp.delete_log()#删除日志
        sleep(2)
        self.assertIn('暂无数据！',lp.assert_delete(self.keyword),msg='删除失败')