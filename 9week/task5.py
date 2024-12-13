"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""


class Solution(object):
    def maxPathSum(self, root):
        self.res = root.val

        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            path = max(node.val + l, node.val + r, node.val)
            self.res = max(self.res, path, node.val + l + r)
            return path

        dfs(root)
        return self.res
