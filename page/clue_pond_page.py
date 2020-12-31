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
    """定位线索池列表表格"""
    table_locator = (By.CSS_SELECTOR, '#form1 > table')
    """定位表格tr标签"""
    tr_locator = (By.TAG_NAME, 'tr')
    """定位td标签"""
    td_locator = (By.TAG_NAME, 'td')
    """定位a标签"""
    a_locator = (By.TAG_NAME, 'a')
    """断言文本定位"""
    assert_locator = (By.CSS_SELECTOR, 'body > div.container > div.alert.alert-success')

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

    def input_input(self, linkman):  # 输入框输入
        self.find_element(self.input_locator).send_keys(linkman)

    def click_search(self):  # 点击【搜索】按钮
        self.find_element(self.search_locator).click()

    def click_amend(self,linkman):  # 点击【修改】按钮
        element = self.find_element(self.table_locator)
        tr_list = self.find_elements(self.tr_locator, element)[2:]
        for tr in tr_list:
            td_list = self.find_elements(self.td_locator, tr)

            if td_list[2].text == linkman:
                self.find_elements(self.a_locator, td_list[9])[2].click()
                break

    def click_back(self):  # 点击【返回】
        self.find_element(self.back_locator).click()

    def click_allocation(self,linkman):  # 点击【分配】
        element = self.find_element(self.table_locator)
        tr_list = self.find_elements(self.tr_locator, element)[2:]
        for tr in tr_list:
            td_list = self.find_elements(self.td_locator, tr)

            if td_list[2].text == linkman:
                self.find_elements(self.a_locator, td_list[9])[4].click()
                break

    def click_ok(self):  # 点击【ok】
        self.find_element(self.ok_locator).click()

    def assert_text(self):  # 获取断言客户名称文本
        txt = self.find_element(self.assert_locator).text.strip()
        return txt.splitlines()[1]

    def clue_pond_flow(self, linkman):  # 线索池流程：新建线索（放入线索池） - 搜索（线索池） - 修改 - 返回 - 分配
        self.click_clue_pond()  # 点击线索池
        sleep(1)
        self.click_new_clue()  # 点击新建线索
        sleep(1)
        self.click_put_clue_pond()  # 点击放入线索池
        sleep(1)
        nc = NEWClue(self.driver)
        nc.input_linkman(linkman)  # 输入联系人
        sleep(1)
        nc.click_sbmit()  # 点击【保存】
        sleep(1)
        self.click_clue_pond()  # 点击【线索池】
        sleep(1)
        self.select_condition()  # 选择筛选条件
        sleep(1)
        self.input_input(linkman)  # 搜索框输入信息
        sleep(1)
        self.click_search()  # 点击【搜索】
        sleep(1)
        self.click_amend(linkman)  # 点击【修改】
        sleep(1)
        self.click_back()  # 点击【返回】
        sleep(1)
        self.click_allocation(linkman)  # 点击【分配】
        sleep(1)
        self.click_ok()  # 点击【ok】

    def clear_data(self):  #清楚数据
        HomePage(self.driver).click_clue()  #返回线索
        sleep(1)

