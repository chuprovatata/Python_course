"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/compare-version-numbers/
"""


class Solution(object):
    def compareVersion(self, version1, version2):
        k1 = 0
        v1 = ["0"]
        for i in range(len(version1)):
            if version1[i] == ".":
                k1 += 1
                v1.append("")
            else:
                v1[k1] += str(version1[i])

        k2 = 0
        v2 = ["0"]
        for i in range(len(version2)):
            if version2[i] == ".":
                k2 += 1
                v2.append("")
            else:
                v2[k2] += str(version2[i])
        maxl = max(len(v1), len(v2))
        if len(v1) < len(v2):
            for i in range(len(v1), len(v2)):
                v1.append("0")
        else:
            for i in range(len(v2), len(v1)):
                v2.append("0")
        for i in range(maxl):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
        return 0
