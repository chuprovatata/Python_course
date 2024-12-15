"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/sum-root-to-leaf-numbers/
"""


class Solution(object):
    def sumNumbers(self, root):
        def dfs(root, num):
            if not root:
                return 0
            num = 10 * num + root.val
            if not root.right and not root.left:
                return num
            return dfs(root.left, num) + dfs(root.right, num)

        return dfs(root, 0)
