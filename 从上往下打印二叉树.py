'''
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root: return []
        que = [root]
        res = []
        while que:
            length = len(que)
            for i in range(length):
                node = que.pop(0)
                res.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return res