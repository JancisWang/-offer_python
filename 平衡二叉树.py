'''
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        self.flag = True
        self.treeiteration(pRoot)
        return self.flag
    def treeiteration(self, root):
        if not root or not self.flag:
            return 0
        left = self.treeiteration(root.left)
        right = self.treeiteration(root.right)
        if abs(left-right)>1:
            self.flag = False
        return 1 + max(left, right)
            
            