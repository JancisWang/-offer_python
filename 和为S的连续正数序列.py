'''
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
输出描述:
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
'''

# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3 : return []
        small = 1
        big = 2
        mid = (1 + tsum) // 2
        sum_ = small + big
        res = []
        while small < mid:
            if sum_ == tsum:
                res.append(list(range(small, big+1)))
                big += 1
                sum_ = sum_ - small + big
                small += 1
            elif sum_ > tsum:
                sum_ -= small
                small += 1
            else:
                big += 1
                sum_ += big
        return res
        
                
            
                            