# coding=utf-8

'''
1. 定义节点类
2. 定义链表类
3. 实例化链表
4. 指定一个节点实例未链表的head
5. 为链表添加节点：实例化一个节点，并指定node.next=second_node
'''


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class ListLink(object):
    def __init__(self,nodes):
        self.head = Node(nodes.pop(0))
        node = self.head
        for i in nodes:
            node.next = Node(i)
            node = node.next


if __name__ == "__main__":
    link = ListLink(['a','b','c'])

    node = link.head
    while node is not None:
        print(node.data)
        node = node.next

