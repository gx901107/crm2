import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep


class Pocess2Test(unittest.TestCase):
    def test_pocess2(self):
        self.driver = webdriver.Chrome()

        self.driver.get("http://192.168.1.213/crm")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        self.driver.find_element(By.NAME, "name").send_keys('xiaodeng')  # 输入用户名
        self.driver.find_element(By.NAME, "password").send_keys('123456')  # 输入密码
        self.driver.find_element(By.NAME, "submit").click()  # 点击登录
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,"#searchForm > div > ul.list0.pull-left > li:nth-child(3) > a").click() #点击crm
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#anchor_42 > div:nth-child(4) > a").click() #点击回复
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#content_42").send_keys('xiaoyouyou') #输入回复
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#reply_42 > div > input.btn.btn-primary.submit").click() #点击评论
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.row > div.span3.knowledgecate > div > div.personal-panel > div:nth-child(2) > p:nth-child(4) > a:nth-child(2)").click() #点击我的日程
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.row > div:nth-child(1) > div > a").click() #点击新建日程
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#subject").send_keys('董事会')  #输入主题
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.row > div > form > table > tfoot > tr > td:nth-child(2) > input:nth-child(1)").click() #点击保存
        sleep(4)
        self.driver.find_element(By.CSS_SELECTOR, "#form1 > table > tbody > tr > td:nth-child(7) > a:nth-child(1)").click() #点击查看日程
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "#tab1 > div.container2.top-pad > div > a:nth-child(2)").click() #点击删除
        sleep(4)
        # self.driver.find_element(By.CSS_SELECTOR, "")
        #
        # self.driver.find_element(By.CSS_SELECTOR, "")
        # self.driver.find_element(By.CSS_SELECTOR, "")
        #
        #
        #
        # self.driver.find_element(By.CSS_SELECTOR, "")

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
        unittest.main()