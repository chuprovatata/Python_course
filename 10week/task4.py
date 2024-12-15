"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/validate-binary-search-tree/
"""


class Solution(object):
    def __init__(self):
        self.prev = -float("inf")

    def isValidBST(self, root):
        if root:
            if not self.isValidBST(root.left):
                return False
            if self.prev >= root.val:
                return False
            self.prev = root.val
            if not self.isValidBST(root.right):
                return False
            return True
        return True
