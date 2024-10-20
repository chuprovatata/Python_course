"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/word-subsets/
"""


class Solution(object):
    def wordSubsets(self, words1, words2):
        res = []
        dictionary = {}
        for i in range(len(words2)):
            for j in range(len(words2[i])):
                if words2[i][j] not in dictionary:
                    dictionary[words2[i][j]] = words2[i].count(words2[i][j])
                elif dictionary[words2[i][j]] < words2[i].count(words2[i][j]):
                    dictionary[words2[i][j]] = words2[i].count(words2[i][j])
        for i in range(len(words1)):
            for j in dictionary:
                if words1[i].count(j) < dictionary[j] or j not in words1[i]:
                    break
            else:
                res.append(words1[i])
        return res
