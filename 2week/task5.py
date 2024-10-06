"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/basic-calculator/
"""


class Solution(object):
    def calculate(self, s):
        stack = []
        sign = 1
        n = 0
        res = 0
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                n = n * 10 + int(char)
            elif char == "+" or char == "-":
                res += sign * n
                n = 0
                sign = 1 if char == "+" else -1
            elif char == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif char == ")":
                res += sign * n
                res *= stack.pop()
                res += stack.pop()
                n = 0
        res += sign * n
        return res
