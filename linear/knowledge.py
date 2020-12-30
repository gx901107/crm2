# -*- coding: utf-8 -*-
# @Time : 2020/12/29 11:25
# @Author : nichao
# @Email : 530504026@qq.com
# @File : knowledge.py
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
knowlede_locator=(By.XPATH,'/html/body/div[1]/div/div/div[2]/ul[1]/li[9]/ul/li[2]/a')#知识定位器
addknowlede_locator=(By.CSS_SELECTOR,'body > div.container > div.row > div:nth-child(2) > div > div.pull-right > a')#添加知识定位器
knowledetitle_locator=(By.ID,'title')#知识标题定位
contentiframe_locator=(By.XPATH,'/html/body/div[5]/div[2]/div/form/table/tbody/tr[4]/td[2]/div/div[2]/iframe')#输入框iframe
content_locator=(By.CSS_SELECTOR,'body')#内容输入框定位器
contentsave_locator=(By.CSS_SELECTOR,'body > div.container > div.row > div > form > table > tfoot > tr > td > input:nth-child(1)')#保存按钮定位器
"""添加知识"""
driver.find_element(*more_locator).click()#点击更多
sleep(1)
driver.find_element(*knowlede_locator).click()#点击知识
sleep(1)
driver.find_element(*addknowlede_locator).click()
sleep(1)
driver.find_element(*knowledetitle_locator).send_keys("运动化")
sleep(1)
driver.switch_to.parent_frame()
driver.switch_to.frame(driver.find_element(*contentiframe_locator))
driver.find_element(*content_locator).send_keys('进行运动会全体员工参与')
sleep(3)
driver.switch_to.parent_frame()
driver.find_element(*contentsave_locator).click()#点击保存按钮
"""查看知识和编辑知识"""
write_locator=(By.LINK_TEXT,'编辑')#查看页面的编辑定位器
knowtitle_locator=(By.NAME,'title')#编辑页面标题输入框定位器
wsave_locator=(By.XPATH,'/html/body/div[5]/div[2]/div/form/table/tfoot/tr/td/input[1]')#编辑保存定位器
knowledline_locator=(By.CSS_SELECTOR,'#form1 > table > tbody')#知识列表的tbody
tr_locator=(By.TAG_NAME,'tr')
td_locator=(By.TAG_NAME,'td')
tr_list=driver.find_element(*knowledline_locator).find_elements(*tr_locator)
for tr in tr_list:
    td_list=tr.find_elements(*td_locator)
    if td_list[1].text=='如何提高客户的满意度':
        td_list[6].find_element(By.CSS_SELECTOR,'a:nth-child(1)').click()
        sleep(1)
        driver.find_element(*write_locator).click()
        sleep(1)
        driver.find_element(*knowtitle_locator).clear()
        driver.find_element(*knowtitle_locator).send_keys('回访客户')
        sleep(1)
        driver.find_element(*wsave_locator).click()
        break
"""搜索知识"""
ksearch_locator=(By.ID,'search')#搜索输入框
sfirst_locator=(By.ID,'field')#搜索第一个下拉框定位器
sseconde_locator=(By.ID,'condition')#第二下拉框的定位器
sbutton_locator=(By.ID,'dosearch')#搜索按钮定位器
Select(driver.find_element(*sfirst_locator)).select_by_visible_text('标题')
Select(driver.find_element(*sseconde_locator)).select_by_visible_text('不包含')
driver.find_element(*ksearch_locator).send_keys('运动')
sleep(1)
driver.find_element(*sbutton_locator).click()
"""删除知识"""
deletebutton_locator=(By.ID,'delete')#删除按钮定位器
deletek_locator=(By.CSS_SELECTOR,'#form1 > table > tbody > tr:nth-child(1) > td:nth-child(1) > input')#要删除的知识的定位器
driver.find_element(*deletek_locator).click()
sleep(1)
driver.find_element(*deletebutton_locator).click()
driver.switch_to.alert.dismiss()
sleep(1)
driver.find_element(*deletebutton_locator).click()
driver.switch_to.alert.accept()
sleep(1)




