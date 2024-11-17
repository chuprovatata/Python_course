"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/arithmetic-slices/
"""


class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        if n < 3:
            return 0
        k = 0
        diff = nums[1] - nums[0]
        length = 2
        for i in range(2, n):
            if nums[i] - nums[i - 1] == diff:
                length += 1
            else:
                if length >= 3:
                    k += (length - 2) * (length - 1) // 2
                diff = nums[i] - nums[i - 1]
                length = 2
        if length >= 3:
            k += (length - 2) * (length - 1) // 2
        return k
