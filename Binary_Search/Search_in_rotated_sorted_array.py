'''
leetcode - 33
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.


'''

from typing import List

class Solution:
    def bs(self, nums, low, high, target):
        if low > high:
            return -1
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[low]:
            if nums[mid] > target and nums[low] <= target:
                return self.bs(nums, low, mid - 1, target)
            else:
                return self.bs(nums, mid + 1, high, target)
        else:
            if nums[mid] < target and nums[high] >= target:
                return self.bs(nums, mid + 1, high, target)
            else:
                return self.bs(nums, low, mid - 1, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.bs(nums, 0, len(nums) - 1, target)