from math import comb
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [[comb(i, j) for j in range(i + 1)] for i in range(rowIndex+1)][rowIndex]


if __name__ == '__main__':
    solution = Solution()
    print(solution.getRow(3))