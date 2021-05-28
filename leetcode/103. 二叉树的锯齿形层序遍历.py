# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # 先层序遍历，再把偶数层结果反转
        stack = [root]
        res = []
        while stack:
            level = []
            for _ in range(len(stack)):
                node = stack.pop(0)
                if not node:
                    continue
                level.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
            if level:
                res.append(level)
        for i in range(1, len(res), 2):
            res[i] = res[i][::-1]
        return res

