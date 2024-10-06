"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/multiply-strings/?source=submission-ac
"""


class Solution(object):
    def multiply(self, num1, num2):
        k = 0
        x1 = 0
        for i in range(len(num1) - 1, -1, -1):
            x1 += int(num1[i]) * 10**k
            k += 1
        k = 0
        x2 = 0
        for i in range(len(num2) - 1, -1, -1):
            x2 += int(num2[i]) * 10**k
            k += 1
        res = str(x1 * x2)
        return res