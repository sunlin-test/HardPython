# coding=utf-8

"""
恶魔天使变装
先选择角色，做出什么事情黑化值、净化值增加或减少，达到峰值，角色转换
角色：恶魔、天使、普通人
实习
"""

blackening_value = 100
purify_value = 100
# todo 恶魔天使变装

class Role(object):
    def __init__(self, role):
        self.role = role
        if role == '恶魔':
            self.blackening_value = 100
            self.purify_value = 0
            self.introduce = "恶魔"
        else:
            self.blackening_value = 0
            self.purify_value = 100
            self.introduce = "天使"


    def check_result(self):
        if self.blackening_value >50 or self.purify_value < 50:
            self.role = "恶魔"

while True:
    your_choose = raw_input("请选择角色> 恶魔 or 天使\n")
    if your_choose not in ("恶魔","天使"):
        print "错啦~ 不支持%s" % your_choose
    else:
        break

you = Role(your_choose)

