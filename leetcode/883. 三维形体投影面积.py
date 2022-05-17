# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/4/26 17:23
from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy = sum(grid[i][j] > 0 for i in range(len(grid)) for j in range(len(grid[0])))
        xz = sum(max(grid[i][j] for i in range(len(grid))) for j in range(len(grid[0])))
        yz = sum(max(grid[i][j] for j in range(len(grid[0]))) for i in range(len(grid)))
        return xy + xz + yz


if __name__ == '__main__':
    s = Solution()
    print(s.projectionArea([[1, 2], [3, 4]]))
