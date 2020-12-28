import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep


class Pocess1Test(unittest.TestCase):
    def test_pocess1(self):
        self.driver = webdriver.Chrome()

        self.driver.get("http://192.168.1.213/crm")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        #登录
        self.driver.find_element(By.NAME,"name").send_keys('xiaodeng') #输入用户名
        self.driver.find_element(By.NAME, "password").send_keys('123456') #输入密码
        self.driver.find_element(By.NAME,"submit").click()  #点击登录
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#searchForm > div > ul.list0.pull-right > li:nth-child(2) > input").send_keys('xiaodeng')  #输入用户名查询动态信息
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,"#searchBtn").click()  #点击查询
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.row > div.span3.knowledgecate > div > div.dynamiccate > ul:nth-child(1) > li:nth-child(1) > a").click() #点击全部
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.row > div.span9 > div > div.pagination > div.span4 > div > ul > li:nth-child(4) > a").click() #点击下一页
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.row > div.span9 > div > div.pagination > div.span4 > div > ul > li:nth-child(2) > a").click() #点击上一页
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.row > div.span9 > div > div.pagination > div.span4 > div > ul > li:nth-child(5) > a").click() #点击末页
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.row > div.span9 > div > div.pagination > div.span4 > div > ul > li:nth-child(1) > a").click() #点击首页
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.row > div.span3.knowledgecate > div > div.personal-panel > div:nth-child(2) > p:nth-child(4) > a:nth-child(1)").click() #点击我的任务
        self.driver.find_element(By.XPATH, "/html/body/div[5]/p/a[1]").click() #点击全部

        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#form1 > table > tbody > tr > td:nth-child(10) > a:nth-child(1)").click() #点击查看任务
        sleep(4)
        self.driver.find_element(By.CSS_SELECTOR,'a[onclick="javascript:history.go(-1)"]').click() #点击返回
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#form1 > table > tbody > tr > td:nth-child(1) > input").click() #勾选第一个任务

        sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, "#delete").click() #点击删除
        sleep(2)

         #获取alert文本
        #self.driver.switch_to.alert.text
        sleep(3)
        self.driver.switch_to.alert.accept() #点击确定
        sleep(5)

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

