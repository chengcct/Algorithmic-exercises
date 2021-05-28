from typing import List


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.count = 0

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.count += 1

        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        self.parent[x_root] = y_root
        self.count -= 1

    def get_count(self):
        return self.count


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind()
        n = len(stones)
        for x, y in stones:
            uf.union(x, y + 10001)
        return n - uf.get_count()


ret = Solution()
print(ret.removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))
