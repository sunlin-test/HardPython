# coding=utf8

"""
恶魔天使变装
先选择角色，做出什么事情黑化值、净化值增加或减少，达到峰值，角色转换
角色：恶魔、天使、普通人
"""

blackening_value = 100
purify_value = 100


class Role:
    def __init__(self, role):
        self.blackening_value = 0
        self.purify_value = 100
        # todo 恶魔天使变装