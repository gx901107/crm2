# -*- coding: utf-8 -*-
# @Time : 2020/12/28 21:25
# @Author : nichao
# @Email : 530504026@qq.com
# @File : organization_2.py.py
# @Project : crm2
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

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
socialavatar_locator = (By.CSS_SELECTOR, '/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/a/img')
driver.find_element_by_css_selector("[class='avatar']").click()  # 点击头像
sleep(3)
origanization_locator = (By.LINK_TEXT, '组织架构')  # 组织架构的定位器
driver.find_element(*origanization_locator).click()  # 点击组织架构
# sleep(3)
# origanization_locator2 = (By.LINK_TEXT, '组织架构')  # 进入组织架构之后的组织架构定位器
# driver.find_element(*origanization_locator2).click()
# sleep(6)
# """编辑部门"""
# huabei_locator = (By.XPATH, '//*[@id="browser"]/li[2]/ul/li[2]/ul/li[2]/span')  # 华北销售部定位器
# locator = driver.find_element(*huabei_locator)
# action = ActionChains(driver)
# sleep(3)
# action.move_to_element(locator).perform()
# sleep(3)
# driver.find_element(*alter_locator).click()
# sleep(6)
# alterpartname_locator = (By.XPATH, '//*[@id="department_edit"]/div[1]/div/input')  # 编辑部门名称定位器
# driver.find_element(*alterpartname_locator).clear()
# sleep(1)
# driver.find_element(*alterpartname_locator).send_keys('华北第一销售部')
# sleep(3)
# alterbutton_locator = (
# By.CSS_SELECTOR, 'body > div:nth-child(13) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix >'
#                  ' div > button:nth-child(1) > span')  # 编辑确定按钮定位器
# sleep(2)
# driver.find_element(*alterbutton_locator).click()
# sleep(3)
# """"删除部门"""
# shichang_locator = (By.XPATH, '//*[@id="browser"]/li[2]/ul/li[2]/ul/li[1]/span')  #卡卡罗特办公室下的市场部定位器
# sc_locator = driver.find_element(*shichang_locator)
# ActionChains(driver).move_to_element(sc_locator).perform()
# sleep(3)
# delete_locator = (By.LINK_TEXT, '删除')  # 删除定位器
# driver.find_element(*delete_locator).click()
# sleep(3)
# driver.switch_to.alert.dismiss()
# sleep(3)
# driver.find_element(*delete_locator).click()
# sleep(3)
# driver.switch_to.alert.accept()
# """编辑岗位"""
# salesspecialist_locator = (By.XPATH, '//*[@id="browser"]/li/ul/li[3]/ul/li[2]/ul/li/ul/li/span')#销售专员定位器
#
# relations_locator = (By.LINK_TEXT, '上下级关系图')  # 上下关系图定位器
# alterrole_locator = (By.LINK_TEXT, '修改')  # 编辑岗位定位器
# altername_locator=(By.ID,'name')#岗位名称输入框
# driver.find_element(*relations_locator).click()#点击上下级关系图
# sleep(3)
# alterrolebutton_locator=(By.XPATH,'/html/body/div[11]/div[3]/div/button[1]')#编辑岗位确定按钮定位器
# ss_locator=driver.find_element(*salesspecialist_locator)
# ActionChains(driver).move_to_element(ss_locator).perform()
# sleep(3)
# driver.find_element(*alterrole_locator).click()#点击编辑
# sleep(2)
# driver.find_element(*altername_locator).clear()
# driver.find_element(*altername_locator).send_keys('销售小组长')
# sleep(3)
# driver.find_element(*alterrolebutton_locator).click()
# sleep(1)
# driver.switch_to.alert.accept()
# sleep(1)
# driver.refresh()
# """删除岗位"""
# ssleader_locator=(By.CSS_SELECTOR,'#browser > li > ul > li.collapsable > ul > li:nth-child(2) > ul > li > ul > li > span')
# sleep(6)
# ActionChains(driver).move_to_element(driver.find_element(*ssleader_locator)).perform()
# sleep(3)
# deletrrole_locator=(By.LINK_TEXT,'删除')
# driver.find_element(*deletrrole_locator).click()
# driver.switch_to.alert.dismiss()
# sleep(2)
# driver.find_element(*deletrrole_locator).click()
# sleep(3)
# driver.switch_to.alert.accept()
# sleep(3)
"""搜索员工"""
usermanagement_locator=(By.LINK_TEXT,'用户管理')#用户管理的定位器
searchuser_locator=(By.CSS_SELECTOR,'#user_form > div:nth-child(1) > ul > li > ul > li > a')#按类别查找的定位器
user_locator=(By.LINK_TEXT,'员工')
driver.find_element(*usermanagement_locator).click()#点击用户管理
sleep(3)
driver.find_element(*searchuser_locator).click()#点击按类别查找
sleep(1)
driver.find_element(*user_locator).click()#点击员工
sleep(3)
aserttable_locator=(By.CSS_SELECTOR,'#user_form > div:nth-child(2) > table > tbody')
tr_locator=(By.TAG_NAME,'tr')
td_locator=(By.TAG_NAME,'td')
aa=driver.find_element(*aserttable_locator)
tr_list=aa.find_elements(*tr_locator)
print(tr_list)
lit=[]
for tr in tr_list:
    td_list=tr.find_elements(*td_locator)
    print(type(td_list[1].text))
    lit.append(td_list[1].text)
print(len(lit))

