"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/maximum-erasure-value/
"""


class Solution(object):
    def maximumUniqueSubarray(self, nums):
        s = set()
        summ = 0
        start = 0
        res = 0
        for i in range(len(nums)):
            while nums[i] in s:
                s.remove(nums[start])
                summ -= nums[start]
                start += 1
            s.add(nums[i])
            summ += nums[i]
            res = max(res, summ)
        return res
