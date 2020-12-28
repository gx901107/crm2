# -*- coding: utf-8 -*-
# @Time : 2020/12/13 20:08
# @Author : fcj11
# @Email : yangfit@126.com
# @File : run_test.py
# @Project : crm自动化测试
import unittest
import time
from BeautifulReport import BeautifulReport
from config.config import REPORT_PATH, CASES_PATH

suite = unittest.defaultTestLoader.discover(CASES_PATH, 'test_case.py')
now_time = time.strftime("%Y%m%d%H%M%S")
filename = f'ecshop-report-{now_time}'
runner = BeautifulReport(suite)
runner.report(description='登录用例自动化测试',
              filename=filename,
              report_dir=REPORT_PATH)
