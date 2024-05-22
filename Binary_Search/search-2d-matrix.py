'''
leetcode- 74
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

'''
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m_l,m_h = 0,len(matrix)-1
        n_l,n_h = 0,len(matrix[0])-1
        while m_l <= m_h:
            mid = m_l + (m_h-m_l)//2
            if matrix[mid][0]<=target and target<=matrix[mid][n_h]:
                m_l = mid
                break
            elif matrix[mid][0] > target:
                m_h = mid - 1
            elif matrix[mid][0] < target:
                m_l = mid + 1
        if m_l > m_h:
            return False
        while n_l <= n_h:
            mid = n_l + (n_h-n_l)//2
            # print(n_l,n_h,mid)
            if matrix[m_l][mid] == target:
                return True
            elif matrix[m_l][mid] > target:
                n_h = mid - 1
            else:
                n_l = mid + 1
            # print(n_l,n_h,mid)
        return False
