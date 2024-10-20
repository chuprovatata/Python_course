"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/first-missing-positive/
"""


class Solution(object):
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums) + 1
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if 0 <= idx < len(nums):
                if nums[idx] > 0:
                    nums[idx] = -nums[idx]
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return len(nums) + 1
