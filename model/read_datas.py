# -*- coding: utf-8 -*-
# @Time : 2020/12/13 18:53
# @Author : fcj11
# @Email : yangfit@126.com
# @File : read_datas.py
# @Project : crm自动化测试

from config.config import DATA_PATH

import xlrd


def read_login_excel(filename=None):
    if not filename:
        filename = DATA_PATH
    data = xlrd.open_workbook(filename + '/login_data.xls')
    table = data.sheet_by_name('login')
    return [table.row_values(line) for line in range(1, table.nrows)]


def read_clue_excel(filename=None):
    if not filename:
        filename = DATA_PATH
    data = xlrd.open_workbook(filename + '/clue_data.xls')
    table = data.sheet_by_name('clue')
    return [table.row_values(line) for line in range(1, table.nrows)]


def read_client_excel(filename=None):
    if not filename:
        filename = DATA_PATH
    data = xlrd.open_workbook(filename + '/client_data.xls')
    table = data.sheet_by_name('client')
    return [table.row_values(line) for line in range(1, table.nrows)]


def read_opportunity_excel(filename=None):
    if not filename:
        filename = DATA_PATH
    data = xlrd.open_workbook(filename + '/opportunity_data.xls')
    table = data.sheet_by_name('opportunity')
    return [table.row_values(line) for line in range(1, table.nrows)]
