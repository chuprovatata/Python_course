"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/generate-parentheses/
"""


class Solution(object):
    def generateParenthesis(self, n):
        res = []

        def backtrack(s, l, r):
            if len(s) == 2 * n:
                res.append(s)
                return res
            if l < n:
                backtrack(s + "(", l + 1, r)

            if r < l:
                backtrack(s + ")", l, r + 1)

        backtrack("", 0, 0)
        return res
