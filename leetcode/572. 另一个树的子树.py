# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def dfs(root, li):
            if root is None:
                return li
            li.append('{' + str(root.val) + '}')
            if root.left is None:
                li.append('LeftNone')
            else:
                dfs(root.left, li)
            if root.right is None:
                li.append('RightNone')
            else:
                dfs(root.right, li)
            return li

        s = ','.join(dfs(s, []))
        t = ','.join(dfs(t, []))
        return t in s
