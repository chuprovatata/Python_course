"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/minimum-size-subarray-sum/
"""


class Solution(object):
    def minSubArrayLen(self, target, nums):
        i = 0
        wsum = 0
        minlen = 100000000
        for j in range(len(nums)):
            wsum += nums[j]
            while wsum >= target:
                minlen = min(minlen, j - i + 1)
                wsum -= nums[i]
                i += 1
        if minlen == 100000000:
            return 0
        else:
            return minlen
