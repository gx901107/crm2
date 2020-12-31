import unittest
from page.login_page import LoginPage
from model.browser import chrome
from model.read_datas import ReadExcel
from page.home_page import HomePage
from time import sleep
from page.affiche_list_page import AfficheListPage
class BashBoardCase(unittest.TestCase):

    def test_dash_board_case(self):
        '''登录'''
        self.driver = chrome()
        lp = LoginPage(self.driver)
        username, password = ReadExcel('login')
        lp.login(username, password)
        #仪表盘-添加组件-添加任务-添加日程-切换到公告列表-添加公告
        hp2=HomePage(self.driver)
        mname,tname,name=ReadExcel('dash_board')
        hp2.homepage2(mname,tname,name)
        sleep(2)
        ap=AfficheListPage(self.driver)
        title,expected=ReadExcel('affiche')
        ap.affichelistpage(title)
        sleep(2)
        #断言
        # expected = '客户满意度调查'
        actual = ap.assert_agin()
        self.assertEqual(expected, actual, msg='添加公告失败')
    def tearDown(self) -> None:
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()