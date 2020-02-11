'''
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot2 or not pRoot1: return False
        return self.isSame(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
    def isSame(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1: return False
        if not root2: return True
        return root1.val == root2.val and self.isSame(root1.left, root2.left) and self.isSame(root1.right, root2.right)