"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/minimum-window-substring/
"""


import collections


class Solution(object):
    def minWindow(self, s, t):
        need = collections.Counter(t)
        l = 0
        r = 0
        i = 0
        j = 0
        missing = len(t)
        while r < len(s):
            if need[s[r]] > 0:
                missing -= 1
            need[s[r]] -= 1
            r += 1
            while missing == 0:
                if j == 0 or r - l < j - i:
                    i, j = l, r
                need[s[l]] += 1
                if need[s[l]] > 0:
                    missing += 1
                l += 1
        return s[i:j]
