"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/largest-time-for-given-digits/description/
"""


class Solution(object):
    def largestTimeFromDigits(self, arr):
        if 2 in arr:
            arr.remove(2)
            n1 = 2
            if 3 in arr:
                arr.remove(3)
                n2 = 3
            elif 2 in arr:
                arr.remove(2)
                n2 = 2
            elif 1 in arr:
                arr.remove(1)
                n2 = 1
            elif 0 in arr:
                n2 = 0
                arr.remove(0)
            else:
                return ""
        elif 1 in arr:
            arr.remove(1)
            n1 = 1
            n2 = max(arr)
            arr.remove(n2)
        elif 0 in arr:
            n1 = 0
            arr.remove(0)
            n2 = max(arr)
            arr.remove(n2)
        else:
            return ""
        if max(arr) < 6:
            n3 = max(arr)
            arr.remove(n3)
            n4 = arr[0]
        elif min(arr) < 6:
            n3 = min(arr)
            arr.remove(n3)
            n4 = arr[0]
        elif n2 == 1 or n2 == 0:
            n3 = n1
            n1 = n2
            n2 = max(arr)
            arr.remove(n2)
            n4 = max(arr)
        else:
            return ""
        first = str(n1) + str(n2)
        second = str(n3) + str(n4)
        res = first + ":" + second
        return res