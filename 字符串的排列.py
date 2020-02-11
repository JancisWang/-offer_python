'''
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''

# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss) <=1 : return ss
        res = []
        for i in range(len(ss)):
            if ss[i]!=ss[0] or i==0:
                for j in map(lambda x: ss[i] + x, self.Permutation(ss[:i] + ss[i+1:])):
                    res.append(j)
        return res
        


            
            
        
        
        
        
        
        