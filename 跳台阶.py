'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
'''

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 2: return number
        dp = [0] * (number + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, number+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
        
        