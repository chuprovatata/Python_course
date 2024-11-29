"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-repeating-character-replacement/
"""


class Solution(object):
    def characterReplacement(self, s, k):
        l = 0
        maxRepeat = 0
        maxLength = 0
        mapper = {}
        for idx, letter in enumerate(s):
            if letter in mapper:
                mapper[letter] += 1
            else:
                mapper[letter] = 1
            maxRepeat = max(maxRepeat, mapper[letter])

            if (idx - l - maxRepeat + 1) > k:
                mapper[s[l]] -= 1
                l += 1
            maxLength = max(maxLength, idx - l + 1)
        return maxLength
