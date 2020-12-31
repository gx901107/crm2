from selenium.webdriver.common.by import By
from page.base_page import BasePage
from time import sleep
class TaskPage(BasePage):
    all_task_locator = (By.XPATH, '/html/body/div[5]/p/a[1]')  # 全部任务
    check_task_locator =(By.CSS_SELECTOR,'#form1 > table > tbody > tr > td:nth-child(10) > a:nth-child(1)') #查看任务
    return_locator= (By.CSS_SELECTOR, 'a[onclick="javascript:history.go(-1)"]') #返回到任务列表
    checkbox_locator = (By.CSS_SELECTOR, '#form1 > table > tbody > tr > td:nth-child(1) > input') #勾选一个任务
    delete_task_locator = (By.CSS_SELECTOR, '#delete') #删除任务
    search_content_locator = (By.CSS_SELECTOR,'#search')  #输入搜索内容
    search_locator=(By.CSS_SELECTOR,'#dosearch')  #点击搜索
    assert_locator=(By.CSS_SELECTOR,'#form1 > table > tbody > tr > td') #获取元素文本
    def all_task_submit(self): #点击全部
        self.find_element(self.all_task_locator).click()
    def check_task_submit(self):  #点击查看任务
        self.find_element(self.check_task_locator).click()
    def return_submit(self):  #点击返回
        self.find_element(self.return_locator).click()
    def checkbox_submit(self): #勾选一个任务
        self.find_element(self.checkbox_locator).click()
    def delete_task_submit(self):  #点击删除
        self.find_element(self.delete_task_locator).click()
    def search_content_input(self,content):  #输入搜索内容
        self.find_element(self.search_content_locator).send_keys(content)
    def search_submit(self): #点击搜索
        self.find_element(self.search_locator).click()
    def search_assert(self):
        return self.find_element(self.assert_locator).text
    def taskpage(self):
        '''点击全部-查看任务-返回-选择一个任务-删除'''
        self.all_task_submit()
        self.check_task_submit()
        sleep(3)
        self.return_submit()
        self.checkbox_submit()
        self.delete_task_submit()
    def taskpage1(self,content):
        '''输入搜索内容-点击搜索'''
        self.search_content_input(content)
        self.search_submit()

