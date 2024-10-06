"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/remove-k-digits/description/
"""


class Solution:
    def removeKdigits(self, num: int, k: int) -> int:
        arr = []
        for digit in num:
            while len(arr) != 0 and arr[-1] > digit and k > 0:
                arr.pop()
                k -= 1
            arr.append(digit)
        while k > 0:
            arr.pop()
            k -= 1
        res = "".join(arr)
        res = res.lstrip("0")
        if res == "":
            return "0"
        else:
            return res