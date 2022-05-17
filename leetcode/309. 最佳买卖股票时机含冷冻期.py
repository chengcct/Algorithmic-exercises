# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/5/12 16:44
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, cd = -prices[0], 0, 0
        for p in prices:
            buy, sell, cd = max(buy, cd - p), max(sell, buy + p), max(sell, cd)
        return max(sell, cd)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([1, 2, 3, 0, 2]))
