"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/repeated-dna-sequences/
"""

from collections import Counter


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10:
            return []
        seen = Counter()
        repeated = set()
        for i in range(len(s) - 9):
            subsequence = s[i : i + 10]
            seen[subsequence] += 1
            if seen[subsequence] > 1:
                repeated.add(subsequence)
        return list(repeated)
