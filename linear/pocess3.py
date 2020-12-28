import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep


class Pocess3Test(unittest.TestCase):
    def test_pocess3(self):
        self.driver = webdriver.Chrome()

        self.driver.get("http://192.168.1.213/crm")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        #登录
        self.driver.find_element(By.NAME,"name").send_keys('xiaodeng') #输入用户名
        self.driver.find_element(By.NAME, "password").send_keys('123456') #输入密码
        self.driver.find_element(By.NAME,"submit").click()  #点击登录
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.page-header > ul > li:nth-child(2) > a").click() #点击仪表盘
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#add").click() #添加组件

        self.driver.find_element(By.CSS_SELECTOR, "#title").send_keys("销售利润") #输入组件名
        sleep(2)
        locator=self.driver.find_element(By.CSS_SELECTOR,"#widget") #定位选择组件
        select=Select(locator)
        select.select_by_index(1) #选择第一个组件
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "#dialog-message > form > div:nth-child(4) > div > input.btn.btn-primary").click() #点击保存
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#calendar > div.c-event-grid > div.c-task-body > div.data-head > a > i").click() #点击快捷添加任务
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#subject").send_keys("小油油研究所")#输入主题
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#owner_name").click() #点击负责人，弹出负责人选择窗口
        sleep(3)

        self.driver.find_element(By.CSS_SELECTOR, "#ta1 > span:nth-child(4) > input").click() #选择负责人
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(12) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(1) > span").click() #点击ok
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.row-fluid > div > form > table > tfoot > tr > td:nth-child(2) > input:nth-child(1)").click() #点击保存
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > a").click()#点击悟空返回到首页
        sleep(2)

        self.driver.find_element(By.CSS_SELECTOR,
                                 "body > div.container > div.page-header > ul > li:nth-child(2) > a").click()  # 点击仪表盘
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#calendar > div.c-event-grid > div.c-event-body > div.data-head > a > i").click() #点击快速添加日程
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#subject").send_keys("员工满意度调查")
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.row > div > form > table > tfoot > tr > td:nth-child(2) > input:nth-child(1)").click() #点击保存
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > a").click()  # 点击悟空返回到首页
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "body > div.container > div.page-header > ul > li:nth-child(2) > a").click()  # 点击仪表盘
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#widgets > div > div:nth-child(6) > div > div.dash-title > a").click() #点击切换到公告列表
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.row > div:nth-child(1) > div.pull-right > a").click() #点击添加公告
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.row > div > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > input").send_keys("优秀员工评选") #输入标题
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.row > div > form > table > tfoot > tr > td > input.btn.btn-primary").click() #点击保存
        sleep(5)
    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
        unittest.main()