"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/largest-number/
"""


class Solution(object):
    def largestNumber(self, l):
        n = len(l)
        for i in range(n):
            for j in range(i + 1, n):
                s = str(l[i]) + str(l[j])
                s1 = str(l[j]) + str(l[i])
                if int(s1) > int(s):
                    k = int(l[i])
                    l[i] = int(l[j])
                    l[j] = int(k)
        res = list(map(str, l))
        if res[0] == "0":
            return "0"
        return "".join(res)
