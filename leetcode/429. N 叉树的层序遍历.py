# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/4/8 16:53
# Definition for a Node.
import collections
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([(root, 0)])
        res = []
        while queue:
            node, deep = queue.popleft()
            if len(res) > deep:
                res[deep].append(node.val)
            else:
                res.append([node.val])
            for child in node.children:
                queue.append((child, deep + 1))
        return res


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node1.children = [node2, node3, node4]
    node2.children = [node5, node6]
    node3.children = [node7]
    solution = Solution()
    print(solution.levelOrder(node1))
