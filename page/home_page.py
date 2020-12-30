# -*- coding: utf-8 -*-
# @Time : 2020/12/12 17:11
# @Author : fcj11
# @Email : yangfit@126.com
# @File : home_page.py
# @Project : crm自动化测试
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from selenium.webdriver.support.select import Select


class HomePage(BasePage):
    '''首页定位器'''
    _url = BasePage._url + '/crm/index.php?m=leads'
    more_locator = (By.XPATH, '/html/body/div[1]/div/div/div[2]/ul[1]/li[9]/a')  # 首页更多定位器
    log_locator = (By.LINK_TEXT, '日志')  # 日志定位器
    knowlede_locator = (By.XPATH, '/html/body/div[1]/div/div/div[2]/ul[1]/li[9]/ul/li[2]/a')  # 知识定位器
    clue_locator = (By.LINK_TEXT, '线索')  # 定位线索
    client_locator = (By.CSS_SELECTOR,
                      'body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul:nth-child(1) > li:nth-child(2) > a')  # 定位客户
    opportunity_locator = (By.CSS_SELECTOR,
                           'body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul:nth-child(1) > li:nth-child(3) > a')  # 定位商机

    searchform_locator = (
    By.CSS_SELECTOR, '#searchForm > div > ul.list0.pull-right > li:nth-child(2) > input')  # 输入查询用户名
    searchbtn_locator = (By.CSS_SELECTOR, '#searchBtn')  # 查询按钮
    all_locator = (By.CSS_SELECTOR,
                   'body > div.container > div.row > div.span3.knowledgecate > div > div.dynamiccate > ul:nth-child(1) > li:nth-child(1) > a')  # 全部动态
    previous_page_locator = (By.CSS_SELECTOR,
                             'body > div.container > div.row > div.span9 > div > div.pagination > div.span4 > div > ul > li:nth-child(4) > a')  # 上一页
    next_page_locator = (By.CSS_SELECTOR,
                         'body > div.container > div.row > div.span9 > div > div.pagination > div.span4 > div > ul > li:nth-child(2) > a')  # 下一页
    last_page_locator = (By.CSS_SELECTOR,
                         'body > div.container > div.row > div.span9 > div > div.pagination > div.span4 > div > ul > li:nth-child(5) > a')  # 末页
    home_page_locator = (By.CSS_SELECTOR,
                         'body > div.container > div.row > div.span9 > div > div.pagination > div.span4 > div > ul > li:nth-child(1) > a')  # 首页
    my_task_locator = (By.CSS_SELECTOR,
                       'body > div.container > div.row > div.span3.knowledgecate > div > div.personal-panel > div:nth-child(2) > p:nth-child(4) > a:nth-child(1)')  # 我的任务
    crm_locator = (By.CSS_SELECTOR, '#searchForm > div > ul.list0.pull-left > li:nth-child(3) > a')  # crm动态
    revert_locator = (By.CSS_SELECTOR, '#anchor_42 > div:nth-child(4) > a')  # 回复
    response_locator = (By.CSS_SELECTOR, '#content_42')  # 输入回复内容
    comment_locator = (By.CSS_SELECTOR, '#reply_42 > div > input.btn.btn-primary.submit')  # 点击评论
    my_schedule_locator = (By.CSS_SELECTOR,
                           'body > div.container > div.row > div.span3.knowledgecate > div > div.personal-panel > div:nth-child(2) > p:nth-child(4) > a:nth-child(2)')  # 我的日程
    dash_board_locator = (By.CSS_SELECTOR, 'body > div.container > div.page-header > ul > li:nth-child(2) > a')  # 仪表盘
    add_module_locator = (By.CSS_SELECTOR, '#add')  # 添加组件
    module_name_locator = (By.CSS_SELECTOR, '#title')  # 输入组件名
    save_locator = (
    By.CSS_SELECTOR, '#dialog-message > form > div:nth-child(4) > div > input.btn.btn-primary')  # 点击保存组件
    add_task_locator = (
    By.CSS_SELECTOR, '#calendar > div.c-event-grid > div.c-task-body > div.data-head > a > i')  # 快捷添加任务
    wukong_locator = (By.CSS_SELECTOR, 'body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > a')  # 点击悟空首页
    add_schedule_locator = (
    By.CSS_SELECTOR, '#calendar > div.c-event-grid > div.c-event-body > div.data-head > a > i')  # 快捷添加日程
    schedule_name_locator = (By.CSS_SELECTOR, '#subject')  # 输入日程主题名
    save_schedule_locator = (By.CSS_SELECTOR,
                             'body > div.container > div.row > div > form > table > tfoot > tr > td:nth-child(2) > input:nth-child(1)')  # 保存新日程
    affiche_list_locator = (By.CSS_SELECTOR, '#widgets > div > div:nth-child(6) > div > div.dash-title > a')  # 切换到公告列表
    head_portrait_locator = (By.CSS_SELECTOR,
                             'body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul.nav.pull-right > li:nth-child(6) > a')  # 点击头像
    my_data_locator = (By.CSS_SELECTOR,
                       'body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul.nav.pull-right > li.dropdown.open > ul > li:nth-child(3) > a')  # 个人资料
    email_locator = (By.CSS_SELECTOR,
                     'body > div.container > div.row > div:nth-child(2) > form > table > tbody > tr:nth-child(11) > td:nth-child(2) > input')  # 邮箱号
    phone_locator = (By.CSS_SELECTOR,
                     'body > div.container > div.row > div:nth-child(2) > form > table > tbody > tr:nth-child(12) > td:nth-child(2) > input')  # 手机号
    save_data_locator = (By.XPATH, '/html/body/div[5]/div[2]/div[2]/form/table/tfoot/tr/td[2]/input[1]')  # 保存修改的个人资料
    organizational_structure_locator = (By.CSS_SELECTOR,
                                        'body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul.nav.pull-right > li.dropdown.open > ul > li:nth-child(4) > a')  # 组织架构
    operation_log_locator = (By.CSS_SELECTOR,
                             'body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul.nav.pull-right > li.dropdown.open > ul > li:nth-child(7) > a')  # 操作日志

    def more_element(self):
        """点击首页更多"""
        self.find_element(self.more_locator).click()  # 点击更多

    def log_element(self):
        self.find_element(self.log_locator).click()  # 点击日志

    def knowlede_element(self):
        self.find_element(self.knowlede_locator).click()  # 点击知识

    def click_clue(self):  # 点击线索
        self.find_element(self.clue_locator).click()

    def click_client(self):  # 点击客户
        self.find_element(self.client_locator).click()

    def click_opportunity(self):  # 点击商机
        self.find_element(self.opportunity_locator).click()

    def searchform_input(self, serchform):  # 输入查询的用户名
        self.find_element(self.searchform_locator).send_keys(serchform)

    def searchbtn_submit(self):  # 点击查询按钮
        self.find_element(self.searchbtn_locator).click()

    def all_submit(self):  # 点击全部动态
        self.find_element(self.all_locator).click()

    def previous_page_submit(self):  # 点击上一页
        self.find_element(self.previous_page_locator).click()

    def next_page_submit(self):  # 点击下一页
        self.find_element(self.next_page_locator).click()

    def last_page_submit(self):  # 点击末页
        self.find_element(self.last_page_locator).click()

    def home_page_submit(self):  # 点击首页，翻页
        self.find_element(self.home_page_locator).click()

    def my_task_submit(self):  # 点击我的任务
        self.find_element(self.my_task_locator).click()

    def crm_submit(self):  # 点击crm动态信息
        self.find_element(self.crm_locator).click()

    def revert_submit(self):  # 点击回复
        self.find_element(self.crm_locator).click()

    def response_input(self, reponse):  # 输入回复内容
        self.find_element(self.response_locator).send_keys(reponse)

    def comment_submit(self):  # 点击评论
        self.find_element(self.comment_locator).click()

    def my_schedule_submit(self):  # 点击我的日程
        self.find_element(self.my_schedule_locator).click()

    def dash_board_submit(self):  # 仪表盘
        self.find_element(self.dash_board_locator).click()

    def add_module_submit(self):  # 点击添加组件
        self.find_element(self.add_module_locator).click()

    def module_name_input(self, mname):  # 输入组件名
        self.find_element(self.module_name_locator).click(mname)

    def select_module(self):
        locator = self.driver.find_element(By.CSS_SELECTOR, "#widget")  # 定位选择组件
        select = Select(locator)
        select.select_by_index(1)  # 选择第一个组件

    def save_submit(self):  # 点击保存按钮
        self.find_element(self.save_locator).click()

    def add_task_submit(self):  # 点击快捷添加任务
        self.find_element(self.add_task_locator).click()

    def wukong_submit(self):  # 点击悟空返回主页
        self.find_element(self.wukong_locator).click()

    def add_schedule_submit(self):  # 快捷添加日程
        self.find_element(self.add_schedule_locator).click()

    def schedule_name_input(self, name):  # 输入日程主题名
        self.find_element(self.schedule_name_locator).send_keys(name)

    def save_schedule_submit(self):  # 点击保存日程
        self.find_element(self.save_schedule_locator).click()

    def affiche_list_submit(self):  # 切换到公告列表
        self.find_element(self.affiche_list_locator).click()

    def head_portrait(self):  # 点击头像
        self.find_element(self.head_portrait_locator).click()

    def my_data_submit(self):  # 点击个人资料
        self.find_element(self.my_data_locator).click()

    def email_input(self, email):  # 邮箱号
        self.find_element(self.email_locator).send_keys(email)

    def phone_input(self, phone):  # 手机号
        self.find_element(self.phone_locator).send_keys(phone)

    def save_data_submit(self):  # 点击保存 保存个人资料
        self.find_element(self.save_data_locator).click()

    def organizational_structure_submit(self):  # 点击组织架构
        self.find_element(self.organizational_structure_locator).click()

    def operation_log_submit(self):  # 点击操作日志
        self.find_element(self.operation_log_locator).click()

    def alert_submit(self):  # 确定警告框
        self.driver.switch_to.alert.accept()

    def homepage(self, searchform):
        '''查询用户日志动态信息-翻页-我的任务'''
        self.searchform_input(searchform)
        self.searchbtn_submit()
        self.all_submit()
        self.previous_page_submit()
        self.next_page_submit()
        self.last_page_submit()
        self.home_page_submit()
        self.my_task_submit()

    def homepage1(self, response):
        '''选择看crm动态信息-回复日志动态-我的日程'''
        self.crm_submit()
        self.revert_submit()
        self.response_input(response)
        self.comment_submit()
        self.my_schedule_submit()

    def homepage2(self, mnane):
        '''仪表盘-添加组件-点击添加问题'''
        self.dash_board_submit()
        self.add_module_submit()
        self.module_name_input(mnane)
        self.select_module()
        self.save_submit()
        self.add_task_submit()

    def homepage3(self, email, phone):
        '''点击头像-个人资料-修改个人资料-点击组织架构'''
        self.head_portrait()
        self.my_data_submit()
        self.email_input(email)
        self.phone_input(phone)
        self.save_data_submit()
        self.head_portrait()
        self.organizational_structure_submit()
