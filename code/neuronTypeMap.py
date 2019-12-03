# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 20:17:06 2019

@author: asus
"""

import xlrd
file = 'data/NeuronType.xls'
def read_neuronType():
    wb = xlrd.open_workbook(filename=file)##打开文件
    sheet = [[]for i in range(12)]
    neuronType = [[]for i in range(12)]
    neuron = [[]for i in range(12)]
    for i in range(12):
        sheet[i] = wb.sheet_by_index(i)
        neuronType[i] = sheet[i].cell_value(0,0)
        neuron[i] = sheet[i].col_values(1)
    d = {}
    i = 0
    for row in neuron:
        for r in row:  
            d[r] = neuronType[i]
        i = i+1
    print(d)
    return d    
if __name__ == '__main__':
    read_neuronType()
    