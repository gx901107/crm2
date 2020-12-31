import unittest
from page.login_page import LoginPage
from model.browser import chrome
from model.read_datas import ReadExcel
from page.home_page import HomePage
from time import sleep
from page.schedule_page import SchedulePage



class WorkTrend1Case(unittest.TestCase):

    def test_work_trend1(self):
        '''登录'''
        self.driver = chrome()
        lp = LoginPage(self.driver)
        username, password = ReadExcel('login')
        lp.login(username, password)
        #查看crm日志-回复日志-点击我的日程
        hp1=HomePage(self.driver)
        response=ReadExcel('response')
        hp1.homepage1(response)
        sleep(2)
        sp=SchedulePage(self.driver)
        sname=ReadExcel('schedule')
        sp.schedulepage(sname)
        sleep(3)
        #断言
        content1,expected =ReadExcel('content1')
        sp.schedulepage1(content1)
        # expected = '----暂无数据！----'
        actual=sp.assert_agin()
        self.assertIn(expected, actual, msg='删除日程失败')
        sleep(2)
    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
