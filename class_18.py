# coding=utf-8

from sys import argv

script, filename = argv

target = open(filename)

print target.read()