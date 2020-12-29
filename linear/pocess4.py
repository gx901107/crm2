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
        # 登录
        self.driver.find_element(By.NAME, "name").send_keys('xiaodeng')  # 输入用户名
        self.driver.find_element(By.NAME, "password").send_keys('123456')  # 输入密码
        self.driver.find_element(By.NAME, "submit").click()  # 点击登录
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul.nav.pull-right > li:nth-child(6) > a").click()  # 点击头像
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul.nav.pull-right > li.dropdown.open > ul > li:nth-child(3) > a").click()  # 点击个人资料
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "body > div.container > div.row > div:nth-child(2) > form > table > tbody > tr:nth-child(11) > td:nth-child(2) > input").clear()
        self.driver.find_element(By.CSS_SELECTOR,
                                 "body > div.container > div.row > div:nth-child(2) > form > table > tbody > tr:nth-child(11) > td:nth-child(2) > input").send_keys(
            "2513011213@qq.com")  # 输入邮箱号
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "body > div.container > div.row > div:nth-child(2) > form > table > tbody > tr:nth-child(12) > td:nth-child(2) > input").clear()
        self.driver.find_element(By.CSS_SELECTOR,
                                 "body > div.container > div.row > div:nth-child(2) > form > table > tbody > tr:nth-child(12) > td:nth-child(2) > input").send_keys(
            "18982859234")  # 输入手机号

        self.driver.find_element(By.XPATH,
                                 "/html/body/div[5]/div[2]/div[2]/form/table/tfoot/tr/td[2]/input[1]").click()  # 点击保存
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul.nav.pull-right > li:nth-child(6) > a").click()  # 点击头像
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul.nav.pull-right > li.dropdown.open > ul > li:nth-child(4) > a").click()  # 点击组织架构
        sleep(2)

        self.driver.find_element(By.CSS_SELECTOR, "#add_role").click()  # 点击添加岗位
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#role_add > div:nth-child(1) > div > input").send_keys(
            "办公室秘书")  # 输入岗位名
        sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[9]/div[3]/div/button[1]/span").click()  # 点击确认
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul.nav.pull-right > li:nth-child(6) > a").click()  # 点击头像
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul.nav.pull-right > li.dropdown.open > ul > li:nth-child(7) > a").click()  # 点击操作日志
        sleep(2)

        self.driver.find_element(By.CSS_SELECTOR,
                                 "body > div.container > div.row > div.span2.knowledgecate > ul > li:nth-child(2) > a").click()  # 按日志类型查看 点击全部
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#form1 > table > tbody > tr:nth-child(1) > td:nth-child(1) > input").click()  # 勾选一个操作日志
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#delete").click()  # 点击删除
        sleep(3)
        self.driver.switch_to.alert.accept()  # 确定警示框
        sleep(5)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
