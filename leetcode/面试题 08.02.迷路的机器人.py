from typing import List


class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        visited = set()

        def dfs(i, j):
            if (i, j) in visited:
                return False
            else:
                visited.add((i, j))
            # 如果到达右下角，且该点为0，返回节点
            while i == row - 1 and j == col - 1 and obstacleGrid[i][j] == 0:
                return [[i, j]]
            # 如果超出边界或该节点为1，返回false
            while i > row - 1 or j > col - 1 or obstacleGrid[i][j] == 1:
                return False
            # 如果都不行，返回空数组
            res = dfs(i, j + 1) or dfs(i + 1, j)
            return [[i, j]] + res if res else []

        res = dfs(0, 0)
        return res if res else []
