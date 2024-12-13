"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/maximum-length-of-repeated-subarray/
"""


class Solution(object):
    def findLength(self, nums1, nums2):
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        max_length = 0
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_length = max(max_length, dp[i][j])
        return max_length
