# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 19:48:23 2019

@author: asus
"""

import xlrd
file = 'data/env.xls'
def read_env():
    wb = xlrd.open_workbook(filename=file)##打开文件
    sheet = wb.sheet_by_index(0)
    data = []
    row = sheet.nrows #获取行数
    for i in range(1,row):
        rowData = sheet.row_values(i)#获取第i行的值
        data.append(rowData)
    # print(data)
    return data    
# if __name__ == '__main__':
#    read_env()