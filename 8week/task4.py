"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
"""


class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        start = 0
        res = 0
        temp = 0
        for end in range(len(arr)):
            temp += arr[end]
            if (end - start + 1) >= k:
                if (temp / k) >= threshold:
                    res += 1
                temp -= arr[start]
                start += 1
        return res
