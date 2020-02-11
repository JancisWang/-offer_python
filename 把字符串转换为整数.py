'''
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
输入描述:
输入一个字符串,包括数字字母符号,可以为空
输出描述:
如果是合法的数值表达则返回该数字，否则返回0
示例1
输入
复制
+2147483647
    1a33
输出
复制
2147483647
    0
'''

# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if not s or s=='+' or s=='-': return 0
        sign = 1
        i = 0
        num = 0
        while i < len(s):
            if i==0 and s[i]=='+':
                i += 1
            elif i==0 and s[i]=='-':
                i += 1
                sign = -1
            elif s[i] >= '0' and s[i] <= '9':
                num = num * 10 + int(s[i])
                if num*sign > 2**31-1 or num*sign < -2**31:
                    return 0
                i += 1
            else:
                return 0
        return num * sign
            

               
                  