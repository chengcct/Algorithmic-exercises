# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/2/15 16:38
from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_row = [min(i) for i in matrix]
        min_col = [max(i) for i in zip(*matrix)]
        print(min_col, min_row)
        return [i for i in min_row if i in min_col]


if __name__ == '__main__':
    res = Solution().luckyNumbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]])
    print(res)
