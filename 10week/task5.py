"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/find-bottom-left-tree-value/
"""


class Solution(object):
    def findBottomLeftValue(self, root):
        q = [root]
        res = []
        while q:
            lenq = len(q)
            a = []
            for i in range(lenq):
                curr = q.pop(0)
                a.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(a)
        return res[-1][0]
