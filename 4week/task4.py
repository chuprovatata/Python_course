"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/rotate-array/
"""


class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        nums[:] = nums[n - k :] + nums[: n - k]
        return nums
