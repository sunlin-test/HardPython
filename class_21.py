# coding=utf-8

from sys import argv
import xlrd

script, filename = argv

plan = xlrd.open_workbook(filename)

sheets = plan.sheet_names()
sheets2 = []
for  i in sheets:
    print i
print type(sheets[0]), type(sheets[1])
for i in sheets:
     sheets2.append(i)
     print sheets2

print sheets2
