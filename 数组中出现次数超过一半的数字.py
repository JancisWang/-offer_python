'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''

# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        d = {}
        for num in numbers:
            if num not in d:
                d[num]=1
            else:
                d[num] += 1
        n = len(numbers)//2
        for key, value in d.items():
            if value > n:
                return key
        return 0


# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        result = numbers[0]
        cnt = 1
        for num in numbers[1:]:
            if num == result:
                cnt += 1
            else:
                cnt -= 1
            if cnt==0:
                result = num
                cnt = 1
        cnt = 0
        for num in numbers:
            if num==result:
                cnt += 1
        if cnt > len(numbers)//2:
            return result
        return 0
                        