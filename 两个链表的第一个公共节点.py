'''
输入两个链表，找出它们的第一个公共结点。
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        def getlength(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        length1 = getlength(pHead1)
        length2 = getlength(pHead2)
        headlong = pHead1
        headshort = pHead2
        lengthdiff = length1 - length2
        if length2 > length1:
            headlong = pHead2
            headshort = pHead1
            lengthdiff = length2 - length1
        for i in range(lengthdiff):
            headlong = headlong.next
        while headlong and headshort and headlong.val != headshort.val:
            headlong = headlong.next
            headshort = headshort.next
        return headlong
                