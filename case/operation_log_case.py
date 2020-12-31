import unittest
from page.login_page import LoginPage
from model.browser import chrome
from model.read_datas import ReadExcel
from page.home_page import HomePage
from time import sleep
from page.organization1_page import OrPage
from page.operation_log_page import OperationLogPage
from model.ncread_datas import read_data_excel
class OperationLogCase(unittest.TestCase):
    driver = chrome()
    def test_operation_log_case(self):
        '''登录'''
        lp = LoginPage(self.driver)
        username, password = ReadExcel('login')
        lp.login(username, password)
        #个人资料-修改个人资料-组织架构-添加架构-添加岗位-操作日志-查询出全部操作日志-删除其中一条操作日志
        hp3=HomePage(self.driver)
        email,phone,expected=ReadExcel('my_data')
        hp3.homepage3(email,phone)
        sleep(2)
        #组织架构添加岗位
        op1=OrPage(self.driver)
        rolename,branch_id,superiorposition_id,roledescription=read_data_excel('addorgan')[1][3:7]
        op1.add_role(rolename,branch_id,superiorposition_id,roledescription)
        #点击头像-操作日志
        hp4=HomePage(self.driver)
        hp4.homepage4()
        sleep(2)
        #查询全部类型的操作日志-删除一个操作日志
        olp=OperationLogPage(self.driver)
        olp.operationlogpage()
        hp4.alert_submit()
        sleep(2)
        #断言
        # expected = '成功删除了相关记录'
        actual = olp.assert_agin()
        self.assertIn(expected, actual, msg='删除操作日志失败')
    def tearDown(self) -> None:
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()
