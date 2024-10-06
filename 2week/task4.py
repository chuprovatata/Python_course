"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""


class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = [""]
        for digit in digits:
            t = []
            for letter in mapping[digit]:
                for combination in res:
                    t.append(combination + letter)
            res = t

        return res
