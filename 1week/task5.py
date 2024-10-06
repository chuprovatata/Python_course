"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/numbers-at-most-n-given-digit-set/
"""


class Solution(object):
    def atMostNGivenDigitSet(self, digits, n):
        num_str = str(n)
        num_len = len(num_str)
        count = 0
        for i in range(1, num_len):
            count += len(digits) ** i
        i = 0
        while i < num_len:
            flag = 0
            for digit in digits:
                if digit < num_str[i]:
                    count += len(digits) ** (num_len - i - 1)
                elif digit == num_str[i]:
                    flag = 1
                    break
                else:
                    break
            if flag == 0:
                break
            i += 1
        if i == num_len:
            count += 1
        return count