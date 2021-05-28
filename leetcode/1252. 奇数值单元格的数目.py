from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        x = [0 for _ in range(n)]
        y = [0 for _ in range(m)]
        for k in indices:
            x[k[0]] = (x[k[0]] + 1) % 2
            y[k[1]] = (y[k[1]] + 1) % 2
        return (len(x) - sum(x)) * sum(y) + sum(x) * (len(y) - sum(y))


ret = Solution()
print(ret.oddCells(2, 3, [[0, 1], [1, 1]]))
