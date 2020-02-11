'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''

# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if matrix ==[[]]: return 
        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = col - 1
        top = 0
        bottom = row - 1
        res = []
        while left < right and top < bottom:
            for j in range(left, right+1):
                res.append(matrix[top][j])
            for i in range(top+1, bottom+1):
                res.append(matrix[i][right])
            for j in range(right-1, left-1, -1):
                res.append(matrix[bottom][j])
            for i in range(bottom-1, top, -1):
                res.append(matrix[i][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        if bottom == top and left < right:
            for j in range(left, right+1):
                res.append(matrix[top][j])
        if left == right and top < bottom:
            for i in range(top, bottom + 1):
                res.append(matrix[i][left])
        if left == right and top == bottom:
            res.append(matrix[top][left])
        return res
                
                
        