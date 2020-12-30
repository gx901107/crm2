from selenium.webdriver.common.by import By
from page.base_page import BasePage
class AfficheListPage(BasePage):
    add_affiche_locator=(By.CSS_SELECTOR,"body > div.container > div.row > div:nth-child(1) > div.pull-right > a")  #添加公告
    title_locator = (By.CSS_SELECTOR, "body > div.container > div.row > div > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > input") #标题名
    save_affiche_locator = (By.CSS_SELECTOR, "body > div.container > div.row > div > form > table > tfoot > tr > td > input.btn.btn-primary") #保存公告
    assert_locator= (By.LINK_TEXT,'客户满意度调查')  #获取元素文本
    def add_affiche_submit(self): #点击添加公告
        self.find_element(self.add_affiche_locator).click()
    def title_input(self,title):  #输入标签名
        self.find_element(self.title_locator).send_keys(title)
    def save_affiche_submit(self):  #点击保存
        self.find_element(self.save_affiche_locator).click()
    def assert_agin(self):  #获取元素文本
        return  self.find_element(self.assert_locator).text

    def affichelistpage(self,title):
        '''添加公告-输入标题名-点击保存'''
        self.add_affiche_submit()
        self.title_input(title)
        self.save_affiche_submit()
