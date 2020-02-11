'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.stack_temp = []
    def push(self, node):
        # write code here
        self.stack.append(node)
    def pop(self):
        # return xx
        if self.stack_temp:
            return self.stack_temp.pop()
        else:
            while self.stack:
                self.stack_temp.append(self.stack.pop())
            return self.stack_temp.pop()
        
   