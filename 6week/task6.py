"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/length-of-the-longest-valid-substring/
"""


class Solution(object):
    def longestValidSubstring(self, word, forbidden):
        length = 0
        all = set()
        for s in forbidden:
            all.add(s)
            length = max(length, len(s))
        res = 0
        r = len(word)
        for i in range(len(word) - 1, -1, -1):
            if r <= res:
                break
            temp = ""
            for j in range(i, min(r, i + length)):
                temp += word[j]
                if temp in all:
                    r = j
                    break
            res = max(res, r - i)
        return res
