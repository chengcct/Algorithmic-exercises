# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from idlelib.tree import TreeNode
from typing import List


class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left_h = self.maxDepth(root.left)
            right_h = self.maxDepth(root.right)
            return max(left_h, right_h) + 1

    def printTree(self, root: TreeNode) -> List[List[str]]:
        if not root:
            return [['']]
        max_depth = self.maxDepth(root)
        m, n = max_depth, (2 ** max_depth - 1)
        res = [[""] * n for _ in range(m)]
        # 层次遍历（depth为深度，index为节点在节点所在层的索引）
        order = []  # 储存存在的节点[深度，值，索引]

        def main(depth, root, index):
            if not root:
                return
            order.append([depth, root.val, index])
            main(depth + 1, root.left, 2 * index)
            main(depth + 1, root.right, 2 * index + 1)
            return

        main(0, root, 0)
        for d, v, i in order:
            i_new = int(((n + 1) / (2 ** (d + 1))) * (2 * i + 1) - 1)
            res[d][i_new] = str(v)
        return res
