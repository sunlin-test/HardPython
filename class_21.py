# coding=utf-8

from sys import argv
import xlrd

script, filename = argv

plan = xlrd.open_workbook(filename)

sheets = plan.sheet_names()
sheets2 = []
print sheets

for i in sheets:
    sheets2.append(i.decode('gb2312').encode('utf-8'))
print sheets2
