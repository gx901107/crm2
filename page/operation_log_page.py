from selenium.webdriver.common.by import By
from page.base_page import BasePage
class OperationLogPage(BasePage):
    all_type_locator = (By.CSS_SELECTOR, "body > div.container > div.row > div.span2.knowledgecate > ul > li:nth-child(2) > a") #全部类型
    check_log_locator = (By.CSS_SELECTOR, "form1 > table > tbody > tr:nth-child(1) > td:nth-child(1) > input") #勾选一个操作日志
    delete_log_locator = (By.CSS_SELECTOR, "#delete")  #删除日志
    def all_type_submit(self):  #点击全部类型
        self.find_element(self.all_type_locator).click()
    def check_log_submit(self):   #勾选一个操作日志
        self.find_element(self.check_log_locator).click()
    def delete_log_submit(self):  #点击删除日志
        self.find_element(self.delete_log_locator).click()
    def operationlogpage(self):
        '''点击全部类型-勾选一个日志-删除日志'''
        self.all_type_submit()
        self.check_log_submit()
        self.delete_log_submit()