"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/unique-binary-search-trees/
"""


class Solution(object):
    def numTrees(self, n):
        if n <= 1:
            return 1
        res = [0] * (n + 1)
        res[0] = 1
        res[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                res[i] += res[i - j] * res[j - 1]
        return res[n]
