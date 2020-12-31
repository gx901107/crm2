# -*- coding: utf-8 -*-
# @Time : 2020/12/30 12:35
# @Author : nichao
# @Email : 530504026@qq.com
# @File : knowledge_page.py
# @Project : crm2
from selenium.webdriver.support.select import Select

from page.base_page import BasePage
from page.home_page import HomePage
from time import sleep
from selenium.webdriver.common.by import By


class KnowledgePage(BasePage):
    alter_locator = (By.LINK_TEXT, '修改')  # 编辑定位器
    addknowlede_locator = (
        By.CSS_SELECTOR, 'body > div.container > div.row > div:nth-child(2) > div > div.pull-right > a')  # 添加知识定位器
    knowledetitle_locator = (By.ID, 'title')  # 知识标题定位
    contentiframe_locator = (
        By.XPATH, '/html/body/div[5]/div[2]/div/form/table/tbody/tr[4]/td[2]/div/div[2]/iframe')  # 输入框iframe
    content_locator = (By.CSS_SELECTOR, 'body')  # 内容输入框定位器
    contentsave_locator = (By.CSS_SELECTOR,
                           'body > div.container > div.row > div > form > table > tfoot > tr > td > input:nth-child(1)')  # 保存按钮定位器

    write_locator = (By.LINK_TEXT, '编辑')  # 查看页面的编辑定位器
    knowtitle_locator = (By.NAME, 'title')  # 编辑页面标题输入框定位器
    wsave_locator = (By.XPATH, '/html/body/div[5]/div[2]/div/form/table/tfoot/tr/td/input[1]')  # 编辑保存定位器
    knowledline_locator = (By.CSS_SELECTOR, '#form1 > table > tbody')  # 知识列表的tbody
    tr_locator = (By.TAG_NAME, 'tr')
    td_locator = (By.TAG_NAME, 'td')
    acheak_locator = (By.CSS_SELECTOR, 'a:nth-child(1)')

    ksearch_locator = (By.ID, 'search')  # 搜索输入框
    sfirst_locator = (By.ID, 'field')  # 搜索第一个下拉框定位器
    sseconde_locator = (By.ID, 'condition')  # 第二下拉框的定位器

    sbutton_locator = (By.ID, 'dosearch')  # 搜索按钮定位器
    deletebutton_locator = (By.ID, 'delete')  # 删除按钮定位器
    deletek_locator = (
        By.CSS_SELECTOR, '#form1 > table > tbody > tr:nth-child(1) > td:nth-child(1) > input')  # 要删除的知识的定位器
    assert_locator = (By.CSS_SELECTOR, '#form1 > table > tbody > tr > td')  # 断言定位器

    def ddknowlede_element(self):  # 点击添加知识
        self.find_element(self.addknowlede_locator).click()

    def knowledetitle_element(self,kntitle):  # 添加知识标题
        self.find_element(self.knowledetitle_locator).send_keys(kntitle)

    def content_element(self,kncontent):  # 输入知识的内容
        self.find_element(self.content_locator).send_keys(kncontent)

    def contentsave_element(self):  # 点击保存按钮
        self.find_element(self.contentsave_locator).click()

    def content(self,kncontent):
        self.switchparent_frame()
        self.switch_frame(self.find_element(self.contentiframe_locator))
        self.content_element(kncontent)  # 输入知识的内容
        self.switchparent_frame()
    def addknowledge(self,kntitle,kncontent):
        self.ddknowlede_element()# 点击添加知识
        sleep(1)
        self.knowledetitle_element(kntitle)#添加知识标题
        sleep(1)
        self.content(kncontent)#输入知识内容
        sleep(1)
        self.contentsave_element()#点击保存
    def write_element(self):  # 查看页面中点击编辑
        self.find_element(self.write_locator).click()

    def knowtitle_element(self,newtitle):  # 编辑知识标题内容
        self.find_element(self.knowtitle_locator).clear()
        self.find_element(self.knowtitle_locator).send_keys(newtitle)

    def wsave_elment(self):  # 点击编辑确认按钮
        self.find_element(self.wsave_locator).click()

    def cheakknowledge(self,newtitle):
        """"查看知识和编辑知识"""
        tr_list = self.find_elements(self.tr_locator,self.find_element(self.knowledline_locator))
        for tr in tr_list:
            td_list = self.find_elements(self.td_locator, tr)
            if td_list[1].text == '如何提高客户的满意度':
                self.find_element(self.acheak_locator,td_list[6]).click()
                sleep(1)
                self.write_element()
                sleep(1)
                self.knowtitle_element(newtitle)
                sleep(1)
                self.wsave_elment()
                break

    def sfirstselect_element(self):  # 搜索按钮的一个下拉框
        return Select(self.find_element(self.sfirst_locator)).select_by_visible_text('标题')

    def secondeselect_element(self):  # 搜索按钮的第二个下拉框
        Select(self.find_element(self.sseconde_locator)).select_by_visible_text('包含')

    def keyword_element(self,knkeyword):  # 搜索输入框的内容
        self.find_element(self.ksearch_locator).send_keys(knkeyword)

    def sbutton_element(self):  # 点击搜索确定按钮
        self.find_element(self.sbutton_locator).click()

    def searchk_element(self,knkeyword):
        """搜索知识"""
        self.sfirstselect_element()  # 搜索按钮的一个下拉框
        sleep(1)
        self.secondeselect_element()  # 搜索按钮的第二个下拉框
        sleep(1)
        self.keyword_element(knkeyword)  # 搜索输入框的内容
        sleep(1)
        self.sbutton_element()  # 点击搜索按钮

    def deletebutton_element(self):  # 删除按钮
        self.find_element(self.deletebutton_locator).click()

    def deletek_element(self):  # 点击要删除的知识
        self.find_element(self.deletek_locator).click()

    def deletekonwledge(self):
        """删除知识"""
        self.deletek_element()  # 点击要删除的知识
        self.deletebutton_element()  # 点击删除按钮
        sleep(2)
        self.switch_dissmiss()  # 点击取消删除
        sleep(1)
        self.deletebutton_element()  # 点击删除按钮
        self.switch_to()  # 点击确定删除
        sleep(1)

    def assertdlete_knoledge(self,knkeyword):
        """断言函数"""
        self.keyword_element(knkeyword) # 搜索输入框的内容
        sleep(1)
        self.sbutton_element()#点击搜索确定按钮
        return self.find_element(self.assert_locator).text.strip()
