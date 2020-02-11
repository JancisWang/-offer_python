'''
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
'''

# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        if not A: return []
        n = len(A)
        C = [1] *n
        D = [1] * n
        B = [0] * n
        for i in range(1, n):
            C[i] = C[i-1] * A[i-1]
        
        for j in range(n-2, -1, -1):
            D[j] = D[j+1] * A[j+1]
        
        for i in range(n):
            B[i] = C[i] * D[i]
        return B
            
            
            