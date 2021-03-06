'''
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot: return None
        if k==0: return None
        res = []
        stack = []
        node = pRoot
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node)
            node = node.right
        if k > len(res): return None
        else: return res[k-1]
       