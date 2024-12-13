"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/deepest-leaves-sum/
"""


class Solution(object):
    def deepestLeavesSum(self, root):
        if root == 0:
            return 0
        queue = [root]
        while queue:
            lenq = len(queue)
            k = []
            for i in range(lenq):
                root = queue.pop(0)
                k.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            if not queue:
                return sum(k)
