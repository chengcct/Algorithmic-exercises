# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/3/21 17:11
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.hashset = set()

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        if k - root.val in self.hashset:
            return True
        self.hashset.add(root.val)
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)

