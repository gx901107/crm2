import unittest
from page.login_page import LoginPage
from model.browser import chrome
from model.read_datas import ReadExcel
from page.home_page import HomePage
from time import sleep
from page.task_page import TaskPage

class WorkTrendCase(unittest.TestCase):
    driver=chrome()
    def test_work_trend(self):
        '''登录'''
        lp=LoginPage(self.driver)
        username,password=ReadExcel('login')
        lp.login(username,password)
        #
        hp=HomePage(self.driver)
        searchform=ReadExcel('work_trend')
        hp.homepage(searchform)
        sleep(5)
        tp=TaskPage(self.driver)
        tp.taskpage()
        hp.alert_submit()
        #断言
        content=ReadExcel('content')
        tp.taskpage1(content)
        tp.search_assert()
        sleep(5)
    def tearDown(self) -> None:
        self.driver.quit()






if __name__ == '__main__':
    unittest.main()
