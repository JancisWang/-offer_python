'''
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''


# 知识点：任何一个数字异或它自己都等于0
# 由于两个数字异或的结果肯定不为0， 那么所有数字异或的结果的二进制表示中至少有一位不为0
# 根据数字中第一位不为1的位的位置，将数组分为两组， 就可以分别得到唯一的两个数字

# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if not array or len(array) < 2:
            return []
        result = 0
        for num in array:
            result ^= num
        
        mask = 1
        while result & mask ==0:
            mask <<= 1
        num1 = num2 = 0
        for num in array:
            if (num & mask) == 0:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]
        
        
