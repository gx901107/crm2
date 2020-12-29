# -*- coding: utf-8 -*-
# @Time : 2020/12/29 0:27
# @Author : nichao
# @Email : 530504026@qq.com
# @File : rizhi.py
# @Project : crm2
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://192.168.1.213/crm')
username_locator = (By.NAME, "name")
password_locator = (By.NAME, 'password')
submit_locator = (By.NAME, 'submit')
alter_locator = (By.LINK_TEXT, '修改')  # 编辑定位器
driver.find_element(*username_locator).send_keys("admin")
driver.find_element(*password_locator).send_keys('123456')
driver.find_element(*submit_locator).click()
sleep(3)
more_locator = (By.XPATH, '/html/body/div[1]/div/div/div[2]/ul[1]/li[9]/a')  # 首页更多定位器
log_locator = (By.LINK_TEXT, '日志')  # 日志定位器
createlog_locator = (By.CSS_SELECTOR, 'body > div.container > div.row > div:nth-child(2) > div > a')  # 新建日志定位器
logtitle_locator = (By.XPATH, '/html/body/div[5]/div[2]/div/form/table/tbody/tr[2]/td[2]/input')  # 日志标题定位器
monthlog_locator = (By.XPATH, '/html/body/div[5]/div[2]/div/form/table/tbody/tr[3]/td[2]/input[4]')  # 月报定位器
logsave_locator = (By.XPATH, '/html/body/div[5]/div[2]/div/form/table/tfoot/tr/td[2]/input[1]')  # 添加日志保存定位器
shurukuang_locator = (
    By.XPATH, '/html/body/div[5]/div[2]/div/form/table/tbody/tr[8]/td[2]/div/div[2]/iframe')  # 日志内容编辑框
driver.find_element(*more_locator).click()  # 点击更多
sleep(3)
driver.find_element(*log_locator).click()  # 点击日志
sleep(2)
driver.find_element(*createlog_locator).click()  # 点击新建日志
sleep(2)
driver.find_element(*logtitle_locator).clear()
driver.find_element(*logtitle_locator).send_keys('3月月报')
sleep(1)
driver.find_element(*monthlog_locator).click()  # 点击月报
sleep(1)
driver.switch_to.parent_frame()
driver.switch_to.frame(driver.find_element(*shurukuang_locator))  # 切换到文本输入框
sleep(3)
driver.find_element_by_xpath('/html/body').send_keys('好困哟')  # 输入日志内容
sleep(3)
driver.switch_to.parent_frame()  # 返回上一级frame
sleep(3)
driver.find_element(*logsave_locator).click()
# """查看日志"""
# sleep(3)
# logtable_locator = (By.XPATH, '//*[@id="form1"]/table/tbody')  # 日志列表的定位器
# tr_locator = (By.TAG_NAME, 'tr')
# td_locator = (By.TAG_NAME, 'td')
# returepage_locator = (By.LINK_TEXT, '返回上一页')
# altertitle_locator = (By.CSS_SELECTOR,
#                       'body > div.container > div.row > div > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > input')
# altertitlesave_locator = (By.XPATH, '/html/body/div[5]/div[2]/div/form/table/tfoot/tr/td[2]/input[1]')
# table_element = driver.find_element(*logtable_locator)
# print(table_element)
# tr_list = driver.find_elements(*tr_locator)[2:]
# print(tr_list, len(tr_list))
# for tr in tr_list:
#     td_list = tr.find_elements(*td_locator)
#     print(td_list)
#     if td_list[2].text == '2020-12-28 工作日志':
#         td_list[6].find_element_by_css_selector('a:nth-child(1)').click()
#         sleep(2)
#         driver.find_element(*returepage_locator).click()
#         break
# """编辑日志"""
# alterreturn_locator=(By.LINK_TEXT,'返回列表页')
# driver.refresh()
# table_element = driver.find_element(*logtable_locator)
# print(table_element)
# tr_list = driver.find_elements(*tr_locator)[2:]
# sleep(3)
# for tr in tr_list:
#     td_list = tr.find_elements(*td_locator)
#     print(td_list)
#     if td_list[2].text == '2020-12-28 工作日志':
#         sleep(3)
#         td_list[6].find_element_by_css_selector('a:nth-child(2)').click()
#         sleep(2)
#         driver.find_element(*altertitle_locator).clear()
#         driver.find_element(*altertitle_locator).send_keys("12-28日志")
#         sleep(2)
#         driver.find_element(*altertitlesave_locator).click()
#         sleep(1)
#         driver.find_element(*alterreturn_locator).click()#点击返回列表
#         break

"""搜索"""
sleep(3)
search_locator=(By.ID,'search')#搜索输入框定位器
searchbutton_locator=(By.CSS_SELECTOR,'#searchForm > ul > li:nth-child(4) > button')#搜索按钮定位器
driver.find_element(*search_locator).send_keys('3月月报')#输入关键子
sleep(2)
driver.find_element(*searchbutton_locator).click()#点击搜索按钮
"""删除"""
delietelog_locator=(By.XPATH,'//*[@id="form1"]/table/tbody/tr[1]/td[1]/input')#删除第一个日志的定位器
deletebutton_locator=(By.CSS_SELECTOR,'#delete')#删除按钮定位器
driver.find_element(*delietelog_locator).click()#选择需要删除的日志
sleep(1)
driver.find_element(*deletebutton_locator).click()
driver.switch_to.alert.dismiss()#点击取消
sleep(1)
driver.find_element(*deletebutton_locator).click()
sleep(1)
driver.switch_to.alert.accept()
sleep(1)
