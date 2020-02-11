'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''

# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers: return ""
        if len(numbers)==1: return str(numbers[0])
        numbers = map(str, numbers)
        
        def quicksort(lst):
            if not lst: return []
            pivot = lst[0]
            left = quicksort([x for x in lst[1:] if x+pivot < pivot+x])
            right = quicksort([x for x in lst[1:] if x+pivot >=pivot+x])
            return left + [pivot] + right
        
        numbers = quicksort(numbers)
        return "".join(numbers)
        
        