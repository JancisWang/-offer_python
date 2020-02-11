'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
输入描述:
题目保证输入的数组中没有的相同的数字

数据范围：

	对于%50的数据,size<=10^4

	对于%75的数据,size<=10^5

	对于%100的数据,size<=2*10^5

示例1
输入
复制
1,2,3,4,5,6,7,0
输出
复制
7
'''

# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        if not data: return 0
        copy = data[:]
        return self.inversecore(data, copy, 0, len(data)-1) % 1000000007
    
    def inversecore(self, data, copy, start, end):
        if start == end:
            copy[start]==data[start]
            return 0
        length = (end - start)//2
        left_cnt = self.inversecore(data, copy, start, start + length)
        right_cnt = self.inversecore(data, copy, start+length+1, end)
        i = start + length
        j = end
        index = end
        count = 0
        while i >= start and j >= start + length + 1:
            if data[i] > data[j]:
                copy[index] = data[i]
                i -= 1
                count += j - start - length
                index -= 1
            else:
                copy[index] = data[j]
                j -= 1
                index -= 1
        while i >= start:
            copy[index] = data[i]
            i -= 1
            index -= 1
        while j >= start + length + 1:
            copy[index] = data[j]
            j -= 1
            index -= 1
        for i in range(start, end+1):
            data[i] = copy[i]
        return (left_cnt + right_cnt + count) 
        
        
        
        