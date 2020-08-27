# coding=utf-8

from sys import argv
import xlrd

script, filename = argv

plan = xlrd.open_workbook(filename)

sheets = plan.sheet_names()
sheets2 = []
print sheets
print type(sheets[0]), type(sheets[1])
for i in sheets:
    sheets2.append(i.encode('utf8'))

print sheets2
