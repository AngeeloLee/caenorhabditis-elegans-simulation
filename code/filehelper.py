# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 19:30:19 2019

@author: asus
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 20:34:28 2019

@author: asus
"""

import xlrd
<<<<<<< HEAD
file = '../data/NeuronConnect.xls'
=======
file = 'data/NeuronConnect.xls'
>>>>>>> 998d43617dad35e85df8ecfb25a5e7cf6de5d7f1
def read_neuronConnet():
    wb = xlrd.open_workbook(filename=file)##打开文件
    datas  = [[]for i in range(16)]
    for i in range(16):
        sheet = wb.sheet_by_index(i)
<<<<<<< HEAD
        count = 418 if i == 15 else 400
        for j in range(count):
            if i==0 and j==0:
                continue
=======
        count = 418 if i ==15 else 400
        for j in range(count):
>>>>>>> 998d43617dad35e85df8ecfb25a5e7cf6de5d7f1
            row = sheet.row_values(j)
            datas[i].append(row)
    print(datas)
    return datas
if __name__ == '__main__':
    read_neuronConnet()
    

        