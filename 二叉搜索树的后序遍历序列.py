'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''

# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence)==0: return False
        n = len(sequence)
        root = sequence[n-1]
        for i in range(n):
            if sequence[i] > root:
                break
        for j in range(i, n):
            if sequence[j] < root:
                return False
        left = True
        if i > 0:
            left  = self.VerifySquenceOfBST(sequence[:i])
        right = True
        if i < n-1:
            right = self.VerifySquenceOfBST(sequence[i:n-1])
        return left and right