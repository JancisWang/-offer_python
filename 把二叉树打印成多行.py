'''
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot: return []
        res = []
        que = [pRoot]
        while que:
            length = len(que)
            temp = []
            for i in range(length):
                node = que.pop(0)
                temp.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(temp)
        return res