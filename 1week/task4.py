"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/reverse-words-in-a-string/?envType=problem-list-v2&envId=string&difficulty=MEDIUM
"""


class Solution(object):
    def reverseWords(self, s):
        arr = s.split()
        res = ""
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] != " ":
                res = res + arr[i] + " "
        res = res[:-1]
        return res