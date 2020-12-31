# -*- coding: utf-8 -*-
# @Time : 2020/12/31 1:55
# @Author : nichao
# @Email : 530504026@qq.com
# @File : ncread_datas.py
# @Project : crm2
import xlrd
from config.config import DATA_PATH


def read_data_excel(sheetname, filename=None):
    if not filename:
        filename = DATA_PATH
    data = xlrd.open_workbook(filename + '/nichao_data.xlsx')
    table = data.sheet_by_name(sheetname)
    return [table.row_values(line) for line in range(0, table.nrows)]



aa=read_data_excel('addorgan')
print(aa)
