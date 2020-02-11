'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
'''

# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if len(tinput)< k or tinput == []: return []
        def quicksort(lst):
            if not lst: return []
            pivot = lst[0]
            left = quicksort([x for x in lst[1:] if x < pivot])
            right = quicksort([x for x in lst[1:] if x > pivot])
            return left + [pivot] + right
        
        tinput = quicksort(tinput)
        return tinput[:k]
       
    