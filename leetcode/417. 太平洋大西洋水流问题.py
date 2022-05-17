# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/4/27 17:10
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def isEmpty(ocean: int, x: int, y: int) -> bool:
            # 找到合法的，没有被统计过的周围的格子
            if x < 0 or x >= m or y < 0 or y >= n:
                return False
            elif CheckMat[x][y][ocean]:
                return False
            else:
                return True

        def searchOneMore(ocean: int, roomList: List[List[int]]) -> List[List[int]]:
            # 对栈中的格子进行一次BFS
            newList = []
            for room in roomList:
                x, y = room[0], room[1]
                for dx, dy in DIREC:
                    nx, ny = x + dx, y + dy
                    if isEmpty(ocean, nx, ny) and heights[nx][ny] >= heights[x][y]:
                        CheckMat[nx][ny][ocean] = True
                        newList.append([nx, ny])
            return newList

        DIREC = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        PACIFIC, ATLANTIC = 0, 1
        m, n = len(heights), len(heights[0])
        CheckMat = [[[False, False] for _ in range(n)] for __ in range(m)]  # [太平洋，大西洋]
        stack, ans = [], []

        # 对能流到太平洋的进行BFS
        for i in range(m):
            CheckMat[i][0][PACIFIC] = True
            stack.append([i, 0])
        for j in range(1, n):
            CheckMat[0][j][PACIFIC] = True
            stack.append([0, j])
        while stack:
            stack = searchOneMore(PACIFIC, stack)

        # 对能流到大西洋的进行BFS
        for i in range(m):
            CheckMat[i][n - 1][ATLANTIC] = True
            stack.append([i, n - 1])
        for j in range(n - 1):
            CheckMat[m - 1][j][ATLANTIC] = True
            stack.append([m - 1, j])
        while stack:
            stack = searchOneMore(ATLANTIC, stack)

        # 统计能流到两个洋的
        for i in range(m):
            for j in range(n):
                if CheckMat[i][j][PACIFIC] and CheckMat[i][j][ATLANTIC]:
                    ans.append([i, j])

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
