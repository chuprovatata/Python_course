"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/coin-change/
"""

import sys


class Solution:
    def coinChange(self, coins, amount):
        n = len(coins)
        w = amount
        t = [[0] * (w + 1)] * (n + 1)
        for i in range(n + 1):
            for j in range(w + 1):
                if i == 0 and j == 0:
                    t[i][j] = 0
                elif j == 0:
                    t[i][j] = 0
                elif i == 0:
                    t[i][j] = sys.maxsize - 1
        for i in range(1, n + 1):
            for j in range(1, w + 1):
                if coins[i - 1] <= j:
                    t[i][j] = min(1 + t[i][j - coins[i - 1]], t[i - 1][j])
                else:
                    t[i][j] = t[i - 1][j]

        return -1 if t[-1][-1] == sys.maxsize - 1 else t[-1][-1]
