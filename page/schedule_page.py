from selenium.webdriver.common.by import By
from page.base_page import BasePage
class SchedulePage(BasePage):
    add_schedule_locator = (By.CSS_SELECTOR, 'body > div.container > div.row > div:nth-child(1) > div > a') #新建日程
    schedule_name_locator = (By.CSS_SELECTOR, '#subject') #输入主题名
    save_schedule_locator = (By.CSS_SELECTOR, 'body > div.container > div.row > div > form > table > tfoot > tr > td:nth-child(2) > input:nth-child(1)') #点击保存
    check_schedule_locator = (By.CSS_SELECTOR, '#form1 > table > tbody > tr > td:nth-child(7) > a:nth-child(1)') #查看日程
    delete_schedule_locator = (By.CSS_SELECTOR, '#tab1 > div.container2.top-pad > div > a:nth-child(2)') #删除
    def add_schedule_submit(self): #点击添加日程
        self.find_element(self.add_schedule_locator).click()
    def schedule_name_input(self,sname): #输入日程主题名
        self.find_element(self.schedule_name_locator).send_keys(sname)
    def save_schedule_submit(self):  #点击保存
        self.find_element(self.save_schedule_locator).click()
    def check_schedule_submit(self): #勾选一个任务
        self.find_element(self.check_schedule_locator).click()
    def delete_schedule_submit(self):  #点击删除
        self.find_element(self.check_schedule_locator).click()
    def schedulepage(self,sname):
        '''添加日程-查看日程-勾选一个日程-删除'''
        self.add_schedule_submit()
        self.schedule_name_input(sname)
        self.save_schedule_submit()
        self.check_schedule_submit()
        self.delete_schedule_submit()
