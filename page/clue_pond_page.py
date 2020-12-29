from time import sleep
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.home_page import HomePage
from page.clue_page import NEWClue
from selenium.webdriver.support.select import Select


class NEWCluePond(BasePage):
    """定位线索池"""
    clue_pond_locator = (By.CSS_SELECTOR, 'body > div.container > div.page-header > ul > li:nth-child(2) > a')
    """定位新建线索"""
    new_clue_locator = (By.CSS_SELECTOR, 'body > div.container > div.row > div:nth-child(1) > div > a')
    """定位放入线索池"""
    put_clue_pond_locator = (By.ID, 'remove')
    """定位联系人姓名输入框"""
    linkman_locator = (By.ID, 'contacts_name')
    """定位保存"""
    submit_locator = (By.NAME, 'submit')
    """定位筛选条件"""
    condition_locator = (By.ID, 'field')
    """定位输入框"""
    input_locator = (By.ID, 'search')
    """定位【搜索】按钮"""
    search_locator = (By.ID, 'dosearch')
    """定位【修改】按钮"""
    amend_locator = (By.LINK_TEXT, '修改')
    """定位【返回】按钮"""
    back_locator = (By.CSS_SELECTOR, 'input[value="返回"]')
    """定位【分配】按钮"""
    allocation_locator = (By.LINK_TEXT, '分配')
    """定位【ok】"""
    ok_locator = (By.CSS_SELECTOR,
                  'body > div:nth-child(11) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(1) > span')

    def click_clue_pond(self):  # 点击线索池
        HomePage(self.driver).click_clue()
        sleep(1)
        self.find_element(self.clue_pond_locator).click()

    def click_new_clue(self):  # 点击新建线索
        self.find_element(self.new_clue_locator).click()

    def click_put_clue_pond(self):  # 点击放入线索池
        self.find_element(self.put_clue_pond_locator).click()
        sleep(1)
        self.switch_to()

    def select_condition(self):  # 筛选条件选择下拉框的索引为3的值
        ct = self.find_element(self.condition_locator)
        Select(ct).select_by_index(3)

    def input_input(self):  # 输入框输入
        self.find_element(self.input_locator).send_keys('张二')

    def click_search(self):  # 点击【搜索】按钮
        self.find_element(self.search_locator).click()

    def click_amend(self):  # 点击【修改】按钮
        self.find_element(self.amend_locator).click()

    def click_back(self):  # 点击【返回】
        self.find_element(self.back_locator).click()

    def click_allocation(self):  # 点击【分配】
        self.find_element(self.allocation_locator).click()

    def click_ok(self):  # 点击【ok】
        self.find_element(self.ok_locator).click()

    def clue_pond_flow(self):  # 线索池流程：新建线索（放入线索池） - 搜索（线索池） - 修改 - 返回 - 分配
        self.click_clue_pond()  # 点击线索池
        sleep(1)
        self.click_new_clue()  # 点击新建线索
        sleep(1)
        self.click_put_clue_pond()  # 点击放入线索池
        sleep(1)
        nc = NEWClue(self.driver)
        nc.input_linkman('张二')  # 输入联系人
        sleep(1)
        nc.click_sbmit()  # 点击【保存】
        sleep(1)
        self.click_clue_pond()  # 点击【线索池】
        sleep(1)
        self.select_condition()  # 选择筛选条件
        sleep(1)
        self.input_input()  # 搜索框输入信息
        sleep(1)
        self.click_search()  # 点击【搜索】
        sleep(1)
        self.click_amend()  # 点击【修改】
        sleep(1)
        self.click_back()  # 点击【返回】
        sleep(1)
        self.click_allocation()  # 点击【分配】
        sleep(1)
        self.click_ok()  # 点击【ok】
