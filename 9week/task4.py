"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/distribute-coins-in-binary-tree/
"""


class Solution(object):
    def distributeCoins(self, root):
        def dfs(root):
            l = 0
            r = 0
            if root.left:
                l = dfs(root.left)
            if root.right:
                r = dfs(root.right)
            ans = l + r + root.val - 1
            self.s += abs(ans)
            return ans

        self.s = 0
        dfs(root)
        return self.s
