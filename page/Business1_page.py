# -*- coding: utf-8 -*-
# @Time : 2020/12/29 21:39
# @Author : 唐涛
# @Email : 2410725336@qq.com
# @File : Business1_page.py
# @Project : crm2
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from page.base_page import BasePage
class Business1Page(BasePage):
    '''商机统计页面类'''
    business_locator=(By.LINK_TEXT,'商机')#商机
    statistics_locator=(By.CSS_SELECTOR,'body > div.container > div.page-header > ul > li:nth-child(2) > a')#统计
    department_locator=(By.CSS_SELECTOR,'#department')#部门
    staff_locator=(By.CSS_SELECTOR,'#role')#员工
    start_time_locator=(By.CSS_SELECTOR,'#start_time')#开始时间
    end_time_locator=(By.CSS_SELECTOR,'#end_time')#结束时间
    search_locator=(By.CSS_SELECTOR,'#searchForm > ul > li:nth-child(4) > button')#搜索
    statistical_content_locator=(By.LINK_TEXT,'选择统计内容')#选择统计内容
    statistical_statement_locator=(By.CSS_SELECTOR,'#show_report')#商机统计报表
    sales_funnel_locator=(By.CSS_SELECTOR,'#show_status')#销售漏斗
    amount_business_locator=(By.CSS_SELECTOR,'#show_money')#商机金额
    sources_statistics_locator=(By.CSS_SELECTOR,'#show_source')#来源统计
    day_tendency_locator=(By.CSS_SELECTOR,'#show_day')#趋势分析按日
    week_tendency_locator=(By.CSS_SELECTOR,'#show_week')#趋势分析按周
    month_tendency_locator=(By.CSS_SELECTOR,'#show_month')#趋势分析按月


    def click_business(self):#商机
        self.find_element(self.business_locator).click()
    def click_statistics(self):#统计
        self.find_element(self.statistics_locator).click()
    def click_department(self):#部门
        select = Select(self.find_element(self.department_locator))
        select.select_by_index(1)
    def click_staff(self):#员工
        select = Select(self.find_element(self.staff_locator))
        select.select_by_index(1)
    def input_start_time(self):#开始时间
        self.find_element(self.staff_locator).send_keys('2020-12-01')
    def input_end_time(self):#结束时间
        self.find_element(self.end_time_locator).send_keys('2020-12-03')
    def click_search(self):#搜索
        self.find_element(self.search_locator).click()
    def click_statistical_content(self):#选择统计内容
        self.find_element(self.statistical_content_locator).click()
    def click_statistical_statement(self):#商机统计报表
        self.find_element(self.statistical_statement_locator).click()
    def click_sales_funnel(self):#销售漏斗
        self.find_element(self.sales_funnel_locator).click()
    def click_amount_business(self):#商机金额
        self.find_element(self.amount_business_locator).click()
    def click_day_tendency(self):#趋势分析按日
        self.find_element(self.day_tendency_locator).click()
    def click_week_tendency(self):#趋势分析按周
        self.find_element(self.week_tendency_locator).click()
    def click_month_tendency(self):#趋势分析按月
        self.find_element(self.month_tendency_locator).click()

    def business1(self):
        self.click_business()#商机
        self.click_statistics()#统计
        self.click_department()#部门
        self.click_staff()#员工
        self.input_start_time()#开始时间
        self.input_end_time()#结束时间
        self.click_search()#搜索
        self.click_statistical_content()#选择统计内容
        self.click_statistical_statement()#商机统计报表
        self.click_sales_funnel()#销售漏斗
        self.click_amount_business()#商机金额
        self.click_day_tendency()#趋势分析按日
        self.click_week_tendency()#趋势分析按周
        self.click_month_tendency()#趋势分析按月



















