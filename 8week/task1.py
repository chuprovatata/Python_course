"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/
"""


class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        count = {}
        res = 0
        l = 0
        for r in range(len(s) + 1):
            if r - l < minSize:
                continue
            sub = s[l:r]
            while minSize <= r - l <= maxSize:
                if len(set(sub)) <= maxLetters:
                    count[sub] = 1 + count.get(sub, 0)
                    res = max(res, count[sub])
                l += 1
                sub = s[l:r]
        return res
