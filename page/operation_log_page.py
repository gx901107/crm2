from selenium.webdriver.common.by import By
from page.base_page import BasePage
from time import sleep
class OperationLogPage(BasePage):
    all_type_locator = (By.CSS_SELECTOR, "body > div.container > div.row > div.span2.knowledgecate > ul > li:nth-child(2) > a") #全部类型
    check_log_locator = (By.XPATH, '//*[@id="form1"]/table/tbody/tr[1]/td[1]/input') #勾选一个操作日志

    delete_log_locator = (By.CSS_SELECTOR, "#delete")  #删除日志
    assert_delete_locator = (By.CSS_SELECTOR,'body > div.container > div.alert.alert-success') #获取删除成功的断言
    def all_type_submit(self):  #点击全部类型
        self.find_element(self.all_type_locator).click()
    def check_log_submit(self):   #勾选一个操作日志
        self.find_element(self.check_log_locator).click()
    def delete_log_submit(self):  #点击删除日志
        self.find_element(self.delete_log_locator).click()
    def assert_agin(self):  #获取删除成功文本
        return self.find_element(self.assert_delete_locator ).text
    def operationlogpage(self):
        '''点击全部类型-勾选一个日志-删除日志'''
        self.all_type_submit()
        sleep(2)
        self.check_log_submit()
        self.delete_log_submit()