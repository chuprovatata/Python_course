"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/binary-tree-right-side-view/
"""


class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        res = []
        res.append(root.val)

        def rightmostNodes(root, depth):
            if not root:
                return
            if depth > len(res):
                res.append(root.val)
            rightmostNodes(root.right, depth + 1)
            rightmostNodes(root.left, depth + 1)

        rightmostNodes(root.right, 2)
        rightmostNodes(root.left, 2)
        return res
