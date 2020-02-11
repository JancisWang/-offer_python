'''
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），每段绳子的长度记为k[0],k[1],...,k[m]。请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
输入描述:
输入一个数n，意义见题面。（2 <= n <= 60）
输出描述:
输出答案。
示例1
输入
复制
8
输出
复制
18
'''

# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        dp = [1] * (number+1)
        dp[1] = 1
        dp[2] = 1
        for i in range(2, number+1):
            res = 0
            for j in range(1, i):
                res = max(res, max(dp[j], j)*max(dp[i-j], i-j))
            dp[i] = res
        return dp[-1]