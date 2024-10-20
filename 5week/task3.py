"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/sort-characters-by-frequency/
"""


class Solution(object):
    def frequencySort(self, s):
        res = ""
        l = sorted(list(set(s)), key=s.count, reverse=True)
        for i in l:
            res += i * s.count(i)
        return res
