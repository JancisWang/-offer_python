'''
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''

# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index ==0: return 0
        res = [1] * index
        nextIndex = 1
        p2 = 0
        p3 = 0
        p5 = 0
        while nextIndex < index:
            nextval = min(res[p2] * 2, res[p3]*3, res[p5]*5)
            res[nextIndex] = nextval
            while res[p2] * 2 <= nextval:
                p2 += 1
            while res[p3] * 3 <= nextval:
                p3 += 1
            while res[p5] * 5 <= nextval:
                p5 += 1
            nextIndex += 1
        return res[-1]
            
            