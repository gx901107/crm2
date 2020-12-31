from selenium.webdriver.common.by import By
from page.base_page import BasePage
from time import sleep
class SchedulePage(BasePage):
    add_schedule_locator = (By.CSS_SELECTOR, 'body > div.container > div.row > div:nth-child(1) > div > a') #新建日程
    schedule_name_locator = (By.CSS_SELECTOR, '#subject') #输入主题名
    save_schedule_locator = (By.CSS_SELECTOR, 'body > div.container > div.row > div > form > table > tfoot > tr > td:nth-child(2) > input:nth-child(1)') #点击保存
    check_schedule_locator = (By.CSS_SELECTOR, '#form1 > table > tbody > tr > td:nth-child(7) > a:nth-child(1)') #查看日程
    delete_schedule_locator = (By.CSS_SELECTOR, '#tab1 > div.container2.top-pad > div > a:nth-child(2)') #删除
    search_content1_locator = (By.CSS_SELECTOR,'#search') #输入搜索内容
    search_locator = (By.CSS_SELECTOR,'#dosearch')  #点击搜索
    assert_locator = (By.CSS_SELECTOR,'#form1 > table > tbody > tr > td') #获取元素文本
    def add_schedule_submit(self): #点击添加日程
        self.find_element(self.add_schedule_locator).click()
    def schedule_name_input(self,sname): #输入日程主题名
        self.find_element(self.schedule_name_locator).send_keys(sname)
    def save_schedule_submit(self):  #点击保存
        self.find_element(self.save_schedule_locator).click()
    def check_schedule_submit(self): #查看日程
        self.find_element(self.check_schedule_locator).click()
    def delete_schedule_submit(self):  #点击删除
        self.find_element(self.delete_schedule_locator).click()
    def search_content1_input(self,content1): #输入搜索内容
        self.find_element(self.search_content1_locator).send_keys(content1)
    def search_submit(self):  #点击搜索
        self.find_element(self.search_locator).click()
    def assert_agin(self):
        return self.find_element(self.assert_locator ).text
    def schedulepage(self,sname):
        '''添加日程-查看日程--删除'''
        self.add_schedule_submit()
        self.schedule_name_input(sname)
        self.save_schedule_submit()
        self.check_schedule_submit()
        sleep(3)
        self.delete_schedule_submit()
    def schedulepage1(self,content1):
        self.search_content1_input(content1)
        self.search_submit()

