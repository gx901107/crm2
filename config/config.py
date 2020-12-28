# -*- coding: utf-8 -*-
# @Time : 2020/12/13 17:30
# @Author : fcj11
# @Email : yangfit@126.com
# @File : config.py
# @Project : crm自动化测试
import os

HOST = 'http://192.168.99.192'
BASE_PATH = os.path.dirname(__file__).strip('config')
REPORT_PATH = os.path.join(BASE_PATH,'report')
CASES_PATH = os.path.join(BASE_PATH, 'cases')
DATA_PATH = os.path.join(BASE_PATH, 'datas')

