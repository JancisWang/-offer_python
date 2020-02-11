'''
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''

# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 2: return number
        m1 = 1
        m2 = 2
        for i in range(3, number+1):
            temp = m2
            m2 += m1
            m1 = temp
        return m2