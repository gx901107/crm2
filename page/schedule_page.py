from selenium.webdriver.common.by import By
from page.base_page import BasePage
class SchedulePage(BasePage):
    add_schedule_locator = (By.CSS_SELECTOR, 'body > div.container > div.row > div:nth-child(1) > div > a') #新建日程
    schedule_name_locator = (By.CSS_SELECTOR, '#subject') #输入主题名
    save_schedule_locator = (By.CSS_SELECTOR, 'body > div.container > div.row > div > form > table > tfoot > tr > td:nth-child(2) > input:nth-child(1)') #点击保存
    check_schedule_locator = (By.CSS_SELECTOR, '#form1 > table > tbody > tr > td:nth-child(7) > a:nth-child(1)') #查看日程
    delete_schedule_locator = (By.CSS_SELECTOR, '#tab1 > div.container2.top-pad > div > a:nth-child(2)') #删除