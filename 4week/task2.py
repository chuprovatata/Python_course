"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/heaters/
"""


class Solution:
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        last = len(heaters) - 1
        x1 = 0
        x2 = 0
        res = 0
        for i in houses:
            while x2 < last and i > heaters[x2]:
                x1 = x2
                x2 = x2 + 1
            d1 = abs(heaters[x1] - i)
            d2 = abs(heaters[x2] - i)
            res = max(res, min(d1, d2))
        return res
