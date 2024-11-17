"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""

from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        if len(s) < len(p):
            return []
        k1 = Counter(p)
        k2 = Counter()
        res = []
        for i in range(len(s)):
            k2[s[i]] += 1
            if i >= len(p):
                if k2[s[i - len(p)]] == 1:
                    del k2[s[i - len(p)]]
                else:
                    k2[s[i - len(p)]] -= 1
            if k1 == k2:
                res.append(i - len(p) + 1)
        return res
