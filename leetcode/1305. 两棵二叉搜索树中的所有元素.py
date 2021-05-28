# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []

        def dfs(root: TreeNode):
            if root is None:
                return True
            res.append(root.val)
            if root.left is not None:
                dfs(root.left)
            if root.right is not None:
                dfs(root.right)
            else:
                return True

        dfs(root1)
        dfs(root2)
        return sorted(res)
