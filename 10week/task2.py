"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root):
        s = ""
        q = deque()
        q.append(root)
        while q:
            n = q.popleft()
            s += ","
            if n is None or not n:
                s += "N"
                continue
            s += str(n.val)
            q.append(n.left)
            q.append(n.right)
        return s

    def deserialize(self, data):
        if len(data) == 0 or data == "" or data == ",N":
            return None
        data = data.split(",")[1:]
        d = data[0]
        root = TreeNode(d)
        q = deque()
        q.append([root, 0])
        q.append([root, 1])
        for d in data[1:]:
            [pointer, flag] = q.popleft()
            if d != "N":
                d = int(d)
                node = TreeNode(d)
                q.append([node, 0])
                q.append([node, 1])
                if flag:
                    pointer.right = node
                else:
                    pointer.left = node
        return root
