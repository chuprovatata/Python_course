"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/minimum-path-sum/
"""


class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        res[0][0] = grid[0][0]
        for i in range(1, n):
            res[0][i] = res[0][i - 1] + grid[0][i]
        for i in range(1, m):
            res[i][0] = res[i - 1][0] + grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                res[i][j] = grid[i][j] + min(res[i - 1][j], res[i][j - 1])
        return res[m - 1][n - 1]
