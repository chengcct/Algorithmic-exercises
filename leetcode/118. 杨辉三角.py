from math import comb
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return [[comb(i, j) for j in range(i + 1)] for i in range(numRows)]


ret = Solution()
print(ret.generate(5))
