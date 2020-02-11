'''
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
'''

# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        def scaninteger(self, start):
            if start > len(s)-1:return start
            if s[start]=='+' or s[start]=='-':
                start += 1
            return self.scanintegeronly(start)
        
        def scanintegeronly(self, start):
            if start > len(s)-1: return start
            while start < len(s)-1 and s[start]>='0' and s[start]<='9':
                start += 1
            return start
        
        if not s: return False
        before = 0
        index = self.scaninteger(0)
        numeric = index > before
        before = index
        if s[index] = '.':
            index = self.scanintegeronly(index+1)
            numeric = index > before + 1 || numeric
            before = index
        if s[index]=='e' or s[index]=='E':
            index = self.scaninteger(index+1)
            numeric = numeric and (index > before + 1)
        return numeric and index==len(s)-1
        
        
        
        