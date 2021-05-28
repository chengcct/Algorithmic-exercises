from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        # 每个点到陆地的曼哈顿距离
        dist = [[float('inf') for _ in range(m)] for _ in range(n)]
        # 该点是否被访问过
        visited = [[False for _ in range(m)] for _ in range(n)]
        q = []
        # 陆地计数
        cnt, ans = 0, 0
        tot = n * m
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    dist[i][j] = 0
                    visited[i][j] = True
                    q.append((i, j))
                    cnt += 1
        # 如果都是陆地或海洋，返回-1
        if cnt == tot or cnt == 0:
            return -1
        while q:
            x, y = q.pop(0)
            for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                # 如果坐标合法且未被访问
                if 0 <= i < n and 0 <= j < m and not visited[i][j]:
                    dist[i][j] = min(dist[i][j], dist[x][y] + 1)
                    ans = max(ans, dist[i][j])
                    visited[i][j] = True
                    q.append((i, j))
        return ans


ret = Solution()
print(ret.maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]))
