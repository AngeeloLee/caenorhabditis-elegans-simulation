# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 20:34:28 2019

@author: asus
"""

import xlrd
file = 'D:\\大学课程学习\\人工智能\\classdesign\\caenorhabditis-elegans-simulation\\data\\NeuronConnect.xls'
def read_excel():
    wb = xlrd.open_workbook(filename=file)##打开文件
    datas  = [[]for i in range(16)]
    for i in range(16):
        sheet = wb.sheet_by_index(i)
        if(i==15):
            for j in range(418):
                row = sheet.row_values(j)
                datas[i].append(row)
        else:
            for j in range(400):
                row = sheet.row_values(j)
                datas[i].append(row)
        print(row)
    print(datas)
    return datas
if __name__ == '__main__':
    read_excel()
    

        