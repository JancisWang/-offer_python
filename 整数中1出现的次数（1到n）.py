'''
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
'''

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        before = 0
        cur = 0
        after = 0
        i = 1
        cnt = 0
        while i <= n:
            before = (n//i)//10
            cur = (n//i) % 10
            after = n - (n//i) * i
            if cur == 0:
                cnt += before * i
            elif cur == 1:
                cnt += before * i + after+1
            else:
                cnt += (before + 1)* i
            i *= 10
        return cnt
            