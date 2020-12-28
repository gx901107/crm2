# -*- coding: utf-8 -*-
# @Time : 2020/12/12 18:47
# @Author : fcj11
# @Email : yangfit@126.com
# @File : browser.py
# @Project : crm自动化测试
from selenium import webdriver

def chrome():  #谷歌
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    return driver