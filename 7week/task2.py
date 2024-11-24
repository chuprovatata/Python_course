"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/subarray-product-less-than-k/
"""


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        l = 0
        r = 0
        prod = 1
        res = 0
        while r < len(nums):
            prod *= nums[r]
            while prod >= k:
                prod /= nums[l]
                l += 1
            res += r - l + 1
            r += 1
        return res
