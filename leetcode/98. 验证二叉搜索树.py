# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            val = node.val
            # 如果当前根节点的值没在正常范围内
            if val <= lower or val >= upper:
                return False
            # 如果左子树的值没在正常范围内
            if not helper(node.left, lower, val):
                return False
            # 如果右子树的值没在正常范围内
            if not helper(node.right, val, upper):
                return False
            return True

        return helper(root)
