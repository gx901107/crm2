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
        #工作动态
        hp=HomePage(self.driver)
        searchform=ReadExcel('work_trend')
        hp.homepage(searchform)
        sleep(2)
        tp=TaskPage(self.driver)
        tp.taskpage()
        hp.alert_submit()
        #断言
        content,expected=ReadExcel('content')
        tp.taskpage1(content)
        sleep(2)
        # expected = '----暂无数据！----'
        actual=tp.search_assert()
        self.assertIn(expected, actual, msg='删除任务失败')
        sleep(2)
    def tearDown(self) -> None:
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()
