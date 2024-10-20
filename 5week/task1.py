"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""


class Solution(object):
    def letterCombinations(self, digits):
        digit_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        for digit in digits:
            letters = digit_letters[digit]
            if len(res) == 0:
                for letter in letters:
                    res.append(letter)
            else:
                res = [
                    current_string + letter
                    for letter in letters
                    for current_string in res
                ]
        return res
