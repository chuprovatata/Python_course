"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/
"""


class Solution(object):
    def maxSum(self, nums, m, k):
        res = 0
        for i in range(len(nums) - k + 1):
            sub_array = nums[i : i + k]
            distinct_count = len(set(sub_array))
            if distinct_count >= m:
                current_sum = sum(sub_array)
                res = max(res, current_sum)

        return res
