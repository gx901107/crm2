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
sleep(3)
origanization_locator2 = (By.LINK_TEXT, '组织架构')  # 进入组织架构之后的组织架构定位器
driver.find_element(*origanization_locator2).click()
sleep(6)
"""编辑部门"""
huabei_locator = (By.XPATH, '//*[@id="browser"]/li[2]/ul/li[2]/ul/li[2]/span')  # 华北销售部定位器
locator = driver.find_element(*huabei_locator)
action = ActionChains(driver)
sleep(3)
action.move_to_element(locator).perform()
sleep(3)
driver.find_element(*alter_locator).click()
sleep(6)
alterpartname_locator = (By.XPATH, '//*[@id="department_edit"]/div[1]/div/input')  # 编辑部门名称定位器
driver.find_element(*alterpartname_locator).clear()
sleep(1)
driver.find_element(*alterpartname_locator).send_keys('华北第一销售部')
sleep(3)
alterbutton_locator = (
By.CSS_SELECTOR, 'body > div:nth-child(13) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix >'
                 ' div > button:nth-child(1) > span')  # 编辑确定按钮定位器
sleep(2)
driver.find_element(*alterbutton_locator).click()
sleep(3)
""""删除部门"""
shichang_locator = (By.XPATH, '//*[@id="browser"]/li[2]/ul/li[2]/ul/li[1]/span')  # 市场部定位器
sc_locator = driver.find_element(*shichang_locator)
ActionChains(driver).move_to_element(sc_locator).perform()
sleep(3)
delete_locator = (By.LINK_TEXT, '删除')  # 删除定位器
driver.find_element(*delete_locator).click()
sleep(3)
driver.switch_to.alert.dismiss()
sleep(3)
driver.find_element(*delete_locator).click()
sleep(3)
driver.switch_to.alert.accept()
"""编辑岗位"""
salesspecialist_locator = (By.XPATH, '//*[@id="browser"]/li/ul/li[3]/ul/li[2]/ul/li/ul/li/span')#销售专员定位器
relations_locator = (By.LINK_TEXT, '上下级关系图')  # 上下关系图定位器
alterrole_locator = (By.LINK_TEXT, '修改')  # 编辑岗位定位器
altername_locator=(By.ID,'name')
driver.find_element(*relations_locator).click()
sleep(3)
alterrolebutton_locator=(By.XPATH,'/html/body/div[11]/div[3]/div/button[1]/span')#编辑岗位确定按钮定位器
ss_locator=driver.find_element(*salesspecialist_locator)
ActionChains(driver).move_to_element(ss_locator).perform()
sleep(3)
driver.find_element(*alterrole_locator).click()#点击编辑