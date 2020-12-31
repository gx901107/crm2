from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from page.base_page import BasePage
from page.home_page import HomePage


class NewClientPond(BasePage):
    """定位器"""
    """【客户池】定位"""
    client_pond_locator = (By.CSS_SELECTOR, 'body > div.container > div.page-header > ul > li:nth-child(2) > a')
    """【新建客户】定位"""
    new_client_locator = (By.CSS_SELECTOR, 'body > div.container > div.row > div:nth-child(1) > div > a')
    """【放入客户池】定位"""
    put_client_pond_locator = (By.ID, 'remove')
    """客户名称输入框定位"""
    client_locator = (By.ID, 'name')
    """【保存】定位"""
    submit_locator = (By.NAME, 'submit')
    """筛选框定位"""
    condition_locator = (By.ID, 'field')
    """定位输入框"""
    input_locator = (By.ID, 'search')
    """【搜索】定位"""
    search_locator = (By.ID, 'dosearch')
    """【编辑】定位"""
    alter_locator = (By.LINK_TEXT, '编辑')
    """定位客户池列表表格"""
    table_locator = (By.CSS_SELECTOR, '#form1 > table')
    """定位表格tr标签"""
    tr_locator = (By.TAG_NAME, 'tr')
    """定位td标签"""
    td_locator = (By.TAG_NAME, 'td')
    """定位a标签"""
    a_locator = (By.TAG_NAME, 'a')
    """【ok】按钮定位"""
    ok_locator = (By.CSS_SELECTOR,
                  'body > div:nth-child(12) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(1) > span')
    """断言文本定位"""
    assert_locator = (By.CSS_SELECTOR, 'body > div.container > div.alert.alert-success')

    def click_client_pond(self):  # 点击【客户池】

        self.find_element(self.client_pond_locator).click()

    def click_new_client(self):  # 点击【新建客户】
        self.find_element(self.new_client_locator).click()

    def click_put_client_pond(self):  # 点击【放入客户池】
        self.find_element(self.put_client_pond_locator).click()

    def input_client(self, clientname):  # 输入客户名
        self.find_element(self.client_locator).send_keys(clientname)

    def click_clear(self):  # 清除客户输入框
        self.find_element(self.client_locator).clear()

    def click_submit(self):  # 点击【保存】
        self.find_element(self.submit_locator).click()

    def click_condition(self):  # 筛选条件下拉框选第二个
        ct = self.find_element(self.condition_locator)
        Select(ct).select_by_index(1)

    def input_input(self, clientname1):  # 输入框输入查找条件
        self.find_element(self.input_locator).send_keys(clientname1)

    def click_search(self):  # 点击搜索
        self.find_element(self.search_locator).click()

    def click_alter(self, clientname1):  # 点击编辑
        element = self.find_element(self.table_locator)
        tr_list = self.find_elements(self.tr_locator, element)[2:]
        for tr in tr_list:
            td_list = self.find_elements(self.td_locator, tr)
            if td_list[1].text == clientname1:
                self.find_elements(self.a_locator, td_list[8])[1].click()
                break

    def click_allocation(self, clientname1):  # 点击分配
        element = self.find_element(self.table_locator)
        tr_list = self.find_elements(self.tr_locator, element)[2:]
        for tr in tr_list:
            td_list = self.find_elements(self.td_locator, tr)
            if td_list[1].text == clientname1:
                self.find_elements(self.a_locator, td_list[8])[2].click()
                break

    def click_ok(self):  # 点击【ok】
        self.find_element(self.ok_locator).click()

    def assert_text(self):  # 获取断言客户名称文本
        txt = self.find_element(self.assert_locator).text.strip()
        return txt.splitlines()[1]

    def client_pond_flow(self, clientname, clientname1):  # 客户池流程：新建客户（放入客户池） - 搜索客户 - 编辑客户 -分配
        HomePage(self.driver).click_client()  # 点击【客户】
        sleep(1)
        self.click_client_pond()  # 点击客户池
        sleep(1)
        self.click_new_client()  # 点击【新建客户】
        sleep(1)
        self.click_put_client_pond()  # 点击【放入客户池】
        sleep(1)
        self.input_client(clientname)  # 输入客户名
        sleep(1)
        self.click_submit()  # 点击保存
        sleep(1)
        self.click_client_pond()  # 点击客户池
        sleep(1)
        self.click_condition()  # 筛选条件选
        sleep(1)
        self.input_input(clientname)  # 输入搜索条件
        sleep(1)
        self.click_search()  # 点击搜索
        sleep(1)
        self.click_alter(clientname)  # 点击编辑
        sleep(1)
        self.click_clear()  # 清除客户名
        sleep(1)
        self.switch_to()  # 确定弹框
        sleep(1)
        self.input_client(clientname1)  # 修改客户名
        sleep(1)
        self.click_submit()  # 保存
        sleep(1)
        self.click_client_pond()  # 点击客户池
        sleep(1)
        self.click_allocation(clientname1)  # 点击【分配】
        sleep(1)
        self.click_ok()  # 点击ok
