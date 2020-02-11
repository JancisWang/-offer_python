'''
统计一个数字在排序数组中出现的次数。
'''

# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        
        def find(lst, k, start, end):
            if not lst: return -1
            while start <= end:
                mid = (end - start) // 2 + start
                if lst[mid] == k:
                    return mid
                elif lst[mid] > k:
                    end = mid - 1
                else:
                    start = mid + 1
            return -1
        
        index = find(data, k, 0, len(data)-1)
        if index == -1 : return 0
        else:
            right = index
            left = index
            while right < len(data) and data[right]==k:
                right += 1
            right -= 1
            while left >= 0 and data[left]==k:
                left -= 1
            left += 1
            return right - left + 1
        

            
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        
        def findfirst(lst, k, start, end):
            if not lst: return -1
            while start <= end:
                mid = (end - start) // 2 + start
                if lst[mid] == k:
                    if (mid > start and lst[mid-1]!=k) or mid==start:
                        return mid
                    else:
                        end = mid - 1
                elif lst[mid] > k:
                    end = mid - 1
                else:
                    start = mid + 1
            return -1
        
        def findlast(lst, k, start, end):
            if not lst: return -1
            while start <= end:
                mid = (end - start) // 2 + start
                if lst[mid] == k:
                    if (mid < end and lst[mid+1]!=k) or mid==end:
                        return mid
                    else:
                        start = mid + 1
                elif lst[mid] > k:
                    end = mid - 1
                else:
                    start = mid + 1
            return -1
        
        first = findfirst(data, k, 0, len(data)-1)
        last = findlast(data, k, 0, len(data)-1)
        
        count = 0
        if first > -1 and last > -1:
            count = last - first + 1
        return count            
            