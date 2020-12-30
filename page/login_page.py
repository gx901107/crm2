# -*- coding: utf-8 -*-
# @Time : 2020/12/12 17:11
# @Author : fcj11
# @Email : yangfit@126.com
# @File : login_page.py
# @Project : crm自动化测试
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from time import sleep
class LoginPage(BasePage):
    _url = BasePage._url + '/crm'

    username_locator = (By.NAME,"name")
    password_locator =(By.NAME,'password')
    submit_locator = (By.NAME,'submit')




    def input_username(self,username):
        self.find_element(self.username_locator).send_keys(username)
    def input_password(self,password):
        self.find_element(self.password_locator).send_keys(int(password))
    def submit(self):
        self.find_element(self.submit_locator).click()
    def open(self):
        self.driver.get(self.url)

    def login(self,username,password):
        self.open()
        self.input_username(username)
        self.input_password(password)
        self.submit()





