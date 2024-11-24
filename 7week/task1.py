"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/find-k-closest-elements/
"""


class Solution(object):
    def findClosestElements(self, arr, k, x):
        l = 0
        r = len(arr) - 1
        while r - l + 1 > k:
            rGap = arr[r] - x
            lGap = x - arr[l]

            if rGap >= lGap:
                r -= 1
            else:
                l += 1
        return arr[l : r + 1]
