"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/binary-tree-level-order-traversal/
"""
from collections import deque


class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        q = deque([root])
        res = []
        while q:
            lenq = len(q)
            temp = []
            for _ in range(lenq):
                n = q.popleft()
                temp.append(n.val)
                if n.left is not None:
                    q.append(n.left)
                if n.right is not None:
                    q.append(n.right)
            res.append(temp)
        return res
